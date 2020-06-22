import sys
import telegram
import worker
import configloader
import utils
import threading
import localization
import logging

try:
    import coloredlogs
except ImportError:
    coloredlogs = None


def main():
    """The core code of the program. Should be run only in the main process!"""
    # Rename the main thread for presentation purposes
    threading.current_thread().name = "Core"

    # Setup logging
    log = logging.getLogger("core")
    logging.root.setLevel(configloader.config["Logging"]["level"])
    stream_handler = logging.StreamHandler()
    if coloredlogs is not None:
        stream_handler.formatter = coloredlogs.ColoredFormatter(configloader.config["Logging"]["format"], style="{")
    else:
        stream_handler.formatter = logging.Formatter(configloader.config["Logging"]["format"], style="{")
    logging.root.handlers.clear()
    logging.root.addHandler(stream_handler)
    log.debug("Logging setup successfully!")

    # Ignore most python-telegram-bot logs, as they are useless most of the time
    logging.getLogger("telegram").setLevel("ERROR")

    # Create a bot instance
    bot = utils.DuckBot(configloader.config["Telegram"]["token"])

    # Test the specified token
    log.debug("Testing bot token...")
    try:
        bot.get_me()
    except telegram.error.Unauthorized:
        logging.fatal("The token you have entered in the config file is invalid. Fix it, then restart greed.")
        sys.exit(1)
    log.debug("Bot token is valid!")

    # Finding default language
    default_language = configloader.config["Language"]["default_language"]
    # Creating localization object
    default_loc = localization.Localization(language=default_language, fallback=default_language)

    # Create a dictionary linking the chat ids to the Worker objects
    # {"1234": <Worker>}
    chat_workers = {}

    # Current update offset; if None it will get the last 100 unparsed messages
    next_update = None

    # Notify on the console that the bot is starting
    log.info("greed is starting!")

    # Main loop of the program
    while True:
        # Get a new batch of 100 updates and mark the last 100 parsed as read
        log.debug("Getting updates from Telegram")
        updates = bot.get_updates(offset=next_update,
                                  timeout=int(configloader.config["Telegram"]["long_polling_timeout"]))
        # Parse all the updates
        for update in updates:
            # If the update is a message...
            if update.message is not None:
                # Ensure the message has been sent in a private chat
                if update.message.chat.type != "private":
                    log.debug(f"Received a message from a non-private chat: {update.message.chat.id}")
                    # Notify the chat
                    bot.send_message(update.message.chat.id, default_loc.get("error_nonprivate_chat"))
                    # Skip the update
                    continue
                # If the message is a start command...
                if isinstance(update.message.text, str) and update.message.text.startswith("/start"):
                    log.info(f"Received /start from: {update.message.chat.id}")
                    # Check if a worker already exists for that chat
                    old_worker = chat_workers.get(update.message.chat.id)
                    # If it exists, gracefully stop the worker
                    if old_worker:
                        log.debug(f"Received request to stop {old_worker.name}")
                        old_worker.stop("request")
                    # Initialize a new worker for the chat
                    new_worker = worker.Worker(bot=bot,
                                               chat=update.message.chat,
                                               telegram_user=update.message.from_user)
                    # Start the worker
                    log.debug(f"Starting {new_worker.name}")
                    new_worker.start()
                    # Store the worker in the dictionary
                    chat_workers[update.message.chat.id] = new_worker
                    # Skip the update
                    continue
                # Otherwise, forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.message.chat.id)
                # Ensure a worker exists for the chat and is alive
                if receiving_worker is None or not receiving_worker.is_alive():
                    log.debug(f"Received a message in a chat without worker: {update.message.chat.id}")
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.message.chat.id, default_loc.get("error_no_worker_for_chat"),
                                     reply_markup=telegram.ReplyKeyboardRemove())
                    # Skip the update
                    continue
                # If the message contains the "Cancel" string defined in the strings file...
                if update.message.text == receiving_worker.loc.get("menu_cancel"):
                    log.debug(f"Forwarding CancelSignal to {receiving_worker}")
                    # Send a CancelSignal to the worker instead of the update
                    receiving_worker.queue.put(worker.CancelSignal())
                else:
                    log.debug(f"Forwarding message to {receiving_worker}")
                    # Forward the update to the worker
                    receiving_worker.queue.put(update)
            # If the update is a inline keyboard press...
            if isinstance(update.callback_query, telegram.CallbackQuery):
                # Forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.callback_query.from_user.id)
                # Ensure a worker exists for the chat
                if receiving_worker is None:
                    log.debug(f"Received a callback query in a chat without worker: {update.callback_query.from_user.id}")
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.callback_query.from_user.id, default_loc.get("error_no_worker_for_chat"))
                    # Skip the update
                    continue
                # Check if the pressed inline key is a cancel button
                if update.callback_query.data == "cmd_cancel":
                    log.debug(f"Forwarding CancelSignal to {receiving_worker}")
                    # Forward a CancelSignal to the worker
                    receiving_worker.queue.put(worker.CancelSignal())
                    # Notify the Telegram client that the inline keyboard press has been received
                    bot.answer_callback_query(update.callback_query.id)
                else:
                    log.debug(f"Forwarding callback query to {receiving_worker}")
                    # Forward the update to the worker
                    receiving_worker.queue.put(update)
            # If the update is a precheckoutquery, ensure it hasn't expired before forwarding it
            if isinstance(update.pre_checkout_query, telegram.PreCheckoutQuery):
                # Forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.pre_checkout_query.from_user.id)
                # Check if it's the active invoice for this chat
                if receiving_worker is None or \
                        update.pre_checkout_query.invoice_payload != receiving_worker.invoice_payload:
                    # Notify the user that the invoice has expired
                    log.debug(f"Received a pre-checkout query for an expired invoice in: {update.message.chat.id}")
                    try:
                        bot.answer_pre_checkout_query(update.pre_checkout_query.id,
                                                      ok=False,
                                                      error_message=default_loc.get("error_invoice_expired"))
                    except telegram.error.BadRequest:
                        log.error("pre-checkout query expired before an answer could be sent!")
                    # Go to the next update
                    continue
                log.debug(f"Forwarding pre-checkout query to {receiving_worker}")
                # Forward the update to the worker
                receiving_worker.queue.put(update)
        # If there were any updates...
        if len(updates):
            # Mark them as read by increasing the update_offset
            next_update = updates[-1].update_id + 1

if __name__ == "__main__":
    # Run the main bot in the main process
    main()
