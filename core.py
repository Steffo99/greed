import sys
import telegram
import worker
import configloader
import utils
import threading
import importlib

language = configloader.config["Config"]["language"]
strings = importlib.import_module("strings." + language)

def main():
    """The core code of the program. Should be run only in the main process!"""

    # Rename the main thread for presentation purposes
    threading.current_thread().name = "Core"

    # Create a bot instance
    bot = utils.DuckBot(configloader.config["Telegram"]["token"])

    # Test the specified token
    try:
        bot.get_me()
    except telegram.error.Unauthorized:
        print("The token you have entered in the config file is invalid.\n"
              "Fix it, then restart this script.")
        sys.exit(1)

    # Create a dictionary linking the chat ids to the ChatWorker objects
    # {"1234": <ChatWorker>}
    chat_workers = {}

    # Current update offset; if None it will get the last 100 unparsed messages
    next_update = None

    # Notify on the console that the bot is starting
    print("greed-bot is now starting!")

    # Main loop of the program
    while True:
        # Get a new batch of 100 updates and mark the last 100 parsed as read
        updates = bot.get_updates(offset=next_update,
                                  timeout=int(configloader.config["Telegram"]["long_polling_timeout"]))
        # Parse all the updates
        for update in updates:
            # If the update is a message...
            if update.message is not None:
                # Ensure the message has been sent in a private chat
                if update.message.chat.type != "private":
                    # Notify the chat
                    bot.send_message(update.message.chat.id, strings.error_nonprivate_chat)
                    # Skip the update
                    continue
                # If the message is a start command...
                if isinstance(update.message.text, str) and update.message.text == "/start":
                    # Check if a worker already exists for that chat
                    old_worker = chat_workers.get(update.message.chat.id)
                    # If it exists, gracefully stop the worker
                    if old_worker:
                        old_worker.stop("request")
                    # Initialize a new worker for the chat
                    new_worker = worker.ChatWorker(bot, update.message.chat)
                    # Start the worker
                    new_worker.start()
                    # Store the worker in the dictionary
                    chat_workers[update.message.chat.id] = new_worker
                    # Skip the update
                    continue
                # Otherwise, forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.message.chat.id)
                # Ensure a worker exists for the chat and is alive
                if receiving_worker is None or not receiving_worker.is_alive():
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.message.chat.id, strings.error_no_worker_for_chat,
                                     reply_markup=telegram.ReplyKeyboardRemove())
                    # Skip the update
                    continue
                # Forward the update to the worker
                receiving_worker.queue.put(update)
            # If the update is a inline keyboard press...
            if isinstance(update.callback_query, telegram.CallbackQuery):
                # Forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.callback_query.from_user.id)
                # Ensure a worker exists for the chat
                if receiving_worker is None:
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.callback_query.from_user.id, strings.error_no_worker_for_chat)
                    # Skip the update
                    continue
                # Check if the pressed inline key is a cancel button
                if update.callback_query.data == "cmd_cancel":
                    # Forward a CancelSignal to the worker
                    receiving_worker.queue.put(worker.CancelSignal())
                    # Notify the Telegram client that the inline keyboard press has been received
                    bot.answer_callback_query(update.callback_query.id)
                else:
                    # Forward the update to the worker
                    receiving_worker.queue.put(update)
            # If the update is a precheckoutquery, ensure it hasn't expired before forwarding it
            if isinstance(update.pre_checkout_query, telegram.PreCheckoutQuery):
                # Forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.pre_checkout_query.from_user.id)
                # Check if it's the active invoice for this chat
                if receiving_worker is None or\
                        update.pre_checkout_query.invoice_payload != receiving_worker.invoice_payload:
                    # Notify the user that the invoice has expired
                    try:
                        bot.answer_pre_checkout_query(update.pre_checkout_query.id,
                                                      ok=False,
                                                      error_message=strings.error_invoice_expired)
                    except telegram.error.BadRequest:
                        print(f"ERROR: pre_checkout_query expired before an answer could be sent")
                    # Go to the next update
                    continue
                # Forward the update to the worker
                receiving_worker.queue.put(update)
        # If there were any updates...
        if len(updates):
            # Mark them as read by increasing the update_offset
            next_update = updates[-1].update_id + 1


# Run the main function only in the main process
if __name__ == "__main__":
    main()
