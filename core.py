import logging
import os, sys
import threading

import sqlalchemy
import sqlalchemy.ext.declarative as sed
import telegram

import database
import duckbot
import localization
import nuconfig
import worker

try:
    import coloredlogs
except ImportError:
    coloredlogs = None


def main():
    """The core code of the program. Should be run only in the main process!"""
    # Rename the main thread for presentation purposes
    threading.current_thread().name = "Core"

    # Start logging setup
    log = logging.getLogger("core")
    logging.root.setLevel("INFO")
    log.debug("Set logging level to INFO while the config is being loaded")

    # Ensure the template config file exists
    if not os.path.isfile("config/template_config.toml"):
        log.fatal("config/template_config.toml does not exist!")
        exit(254)

    # Check where the config path is located from the CONFIG_PATH environment variable
    config_path = os.environ.get("CONFIG_PATH", "config/config.toml")

    # If the config file does not exist, clone the template and exit
    if not os.path.isfile(config_path):
        log.debug("config/config.toml does not exist.")

        with open("config/template_config.toml", encoding="utf8") as template_cfg_file, \
                open(config_path, "w", encoding="utf8") as user_cfg_file:
            # Copy the template file to the config file
            user_cfg_file.write(template_cfg_file.read())

        log.fatal("A config file has been created."
                  " Customize it, then restart greed!")
        exit(1)

    # Compare the template config with the user-made one
    with open("config/template_config.toml", encoding="utf8") as template_cfg_file, \
            open(config_path, encoding="utf8") as user_cfg_file:
        template_cfg = nuconfig.NuConfig(template_cfg_file)
        user_cfg = nuconfig.NuConfig(user_cfg_file)
        if not template_cfg.cmplog(user_cfg):
            log.fatal("There were errors while parsing the config file. Please fix them and restart greed!")
            exit(2)
        else:
            log.debug("Configuration parsed successfully!")

    # Finish logging setup
    logging.root.setLevel(user_cfg["Logging"]["level"])
    stream_handler = logging.StreamHandler()
    if coloredlogs is not None:
        stream_handler.formatter = coloredlogs.ColoredFormatter(user_cfg["Logging"]["format"], style="{")
    else:
        stream_handler.formatter = logging.Formatter(user_cfg["Logging"]["format"], style="{")
    logging.root.handlers.clear()
    logging.root.addHandler(stream_handler)
    log.debug("Logging setup successfully!")

    # Ignore most python-telegram-bot logs, as they are useless most of the time
    logging.getLogger("telegram").setLevel("ERROR")

    # Find the database URI
    # Through environment variables first
    if db_engine := os.environ.get("DB_ENGINE"):
        log.debug("Sqlalchemy engine overridden by the DB_ENGINE envvar.")
    # Then via the config file
    else:
        db_engine = user_cfg["Database"]["engine"]
        log.debug("Using sqlalchemy engine set in the configuration file.")

    # Create the database engine
    log.debug("Creating the sqlalchemy engine...")
    engine = sqlalchemy.create_engine(db_engine)
    log.debug("Binding metadata to the engine...")
    database.TableDeclarativeBase.metadata.bind = engine
    log.debug("Creating all missing tables...")
    database.TableDeclarativeBase.metadata.create_all()
    log.debug("Preparing the tables through deferred reflection...")
    sed.DeferredReflection.prepare(engine)

    # Create a bot instance
    bot = duckbot.factory(user_cfg)(request=telegram.utils.request.Request(user_cfg["Telegram"]["con_pool_size"]))

    # Test the specified token
    log.debug("Testing bot token...")
    me = bot.get_me()
    if me is None:
        logging.fatal("The token you have entered in the config file is invalid. Fix it, then restart greed.")
        sys.exit(1)
    log.debug("Bot token is valid!")

    # Finding default language
    default_language = user_cfg["Language"]["default_language"]
    # Creating localization object
    default_loc = localization.Localization(language=default_language, fallback=default_language)

    # Create a dictionary linking the chat ids to the Worker objects
    # {"1234": <Worker>}
    chat_workers = {}

    # Current update offset; if None it will get the last 100 unparsed messages
    next_update = None

    # Notify on the console that the bot is starting
    log.info(f"@{me.username} is starting!")

    # Main loop of the program
    while True:
        # Get a new batch of 100 updates and mark the last 100 parsed as read
        update_timeout = user_cfg["Telegram"]["long_polling_timeout"]
        log.debug(f"Getting updates from Telegram with a timeout of {update_timeout} seconds")
        updates = bot.get_updates(offset=next_update,
                                  timeout=update_timeout)
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
                                               telegram_user=update.message.from_user,
                                               cfg=user_cfg,
                                               engine=engine,
                                               daemon=True)
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
                if receiving_worker is None:
                    log.debug(f"Received a message in a chat without worker: {update.message.chat.id}")
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.message.chat.id, default_loc.get("error_no_worker_for_chat"),
                                     reply_markup=telegram.ReplyKeyboardRemove())
                    # Skip the update
                    continue
                # If the worker is not ready...
                if not receiving_worker.is_ready():
                    log.debug(f"Received a message in a chat where the worker wasn't ready yet: {update.message.chat.id}")
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.message.chat.id, default_loc.get("error_worker_not_ready"),
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
                    log.debug(
                        f"Received a callback query in a chat without worker: {update.callback_query.from_user.id}")
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
                    log.debug(f"Received a pre-checkout query for an expired invoice in: {update.pre_checkout_query.from_user.id}")
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


# Run the main function only in the main process
if __name__ == "__main__":
    main()
