import logging
import sys, time
import traceback

import telegram.error

import nuconfig

log = logging.getLogger(__name__)


def factory(cfg: nuconfig.NuConfig):
    """Construct a DuckBot type based on the passed config."""

    def catch_telegram_errors(func):
        """Decorator, can be applied to any function to retry in case of Telegram errors."""

        def result_func(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                # Bot was blocked by the user
                except telegram.error.Unauthorized:
                    log.debug(f"Unauthorized to call {func.__name__}(), skipping.")
                    return None
                # Telegram API didn't answer in time
                except telegram.error.TimedOut:
                    log.warning(f"Timed out while calling {func.__name__}(),"
                                f" retrying in {cfg['Telegram']['timed_out_pause']} secs...")
                    time.sleep(cfg["Telegram"]["timed_out_pause"])
                    continue
                # Telegram is not reachable
                except telegram.error.NetworkError as error:
                    log.error(f"Network error while calling {func.__name__}(),"
                              f" retrying in {cfg['Telegram']['error_pause']} secs...\n"
                              f"Full error: {error.message}")
                    time.sleep(cfg["Telegram"]["error_pause"])
                    continue
                # Unknown error
                except telegram.error.TelegramError as error:
                    if error.message.lower() in ["bad gateway", "invalid server response"]:
                        log.warning(f"Bad Gateway while calling {func.__name__}(),"
                                    f" retrying in {cfg['Telegram']['error_pause']} secs...")
                        time.sleep(cfg["Telegram"]["error_pause"])
                        continue
                    elif error.message.lower() == "timed out":
                        log.warning(f"Timed out while calling {func.__name__}(),"
                                    f" retrying in {cfg['Telegram']['timed_out_pause']} secs...")
                        time.sleep(cfg["Telegram"]["timed_out_pause"])
                        continue
                    else:
                        log.error(f"Telegram error while calling {func.__name__}(),"
                                  f" retrying in {cfg['Telegram']['error_pause']} secs...\n"
                                  f"Full error: {error.message}")
                        traceback.print_exception(*sys.exc_info())
                        time.sleep(cfg["Telegram"]["error_pause"])
                        continue

        return result_func

    class DuckBot:
        def __init__(self, *args, **kwargs):
            self.bot = telegram.Bot(token=cfg["Telegram"]["token"], *args, **kwargs)

        @catch_telegram_errors
        def send_message(self, *args, **kwargs):
            # All messages are sent in HTML parse mode
            return self.bot.send_message(parse_mode="HTML", *args, **kwargs)

        @catch_telegram_errors
        def send_photo(self, *args, **kwargs):
            return self.bot.send_photo(parse_mode="HTML", *args, **kwargs)

        @catch_telegram_errors
        def edit_message_text(self, *args, **kwargs):
            # All messages are sent in HTML parse mode
            return self.bot.edit_message_text(parse_mode="HTML", *args, **kwargs)

        @catch_telegram_errors
        def edit_message_caption(self, *args, **kwargs):
            # All messages are sent in HTML parse mode
            return self.bot.edit_message_caption(parse_mode="HTML", *args, **kwargs)

        @catch_telegram_errors
        def edit_message_reply_markup(self, *args, **kwargs):
            return self.bot.edit_message_reply_markup(*args, **kwargs)

        @catch_telegram_errors
        def get_updates(self, *args, **kwargs):
            return self.bot.get_updates(*args, **kwargs)

        @catch_telegram_errors
        def get_me(self, *args, **kwargs):
            return self.bot.get_me(*args, **kwargs)

        @catch_telegram_errors
        def answer_callback_query(self, *args, **kwargs):
            return self.bot.answer_callback_query(*args, **kwargs)

        @catch_telegram_errors
        def answer_pre_checkout_query(self, *args, **kwargs):
            return self.bot.answer_pre_checkout_query(*args, **kwargs)

        @catch_telegram_errors
        def send_invoice(self, *args, **kwargs):
            return self.bot.send_invoice(*args, **kwargs)

        @catch_telegram_errors
        def get_file(self, *args, **kwargs):
            return self.bot.get_file(*args, **kwargs)

        @catch_telegram_errors
        def send_chat_action(self, *args, **kwargs):
            return self.bot.send_chat_action(*args, **kwargs)

        @catch_telegram_errors
        def delete_message(self, *args, **kwargs):
            return self.bot.delete_message(*args, **kwargs)

        @catch_telegram_errors
        def send_document(self, *args, **kwargs):
            return self.bot.send_document(*args, **kwargs)

        # More methods can be added here

    return DuckBot
