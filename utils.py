import telegram
import telegram.error
import time
from configloader import config
import typing
import os
import sys
import importlib
import logging
import traceback
import localization


log = logging.getLogger(__name__)


if config["Error Reporting"]["sentry_token"] != \
        "https://00000000000000000000000000000000:00000000000000000000000000000000@sentry.io/0000000":
    import raven
    import raven.exceptions
    try:
        release = raven.fetch_git_sha(os.path.dirname(__file__))
    except raven.exceptions.InvalidGitRepository:
        release = "Unknown"
    sentry_client = raven.Client(config["Error Reporting"]["sentry_token"],
                                 release=release,
                                 environment="Dev" if __debug__ else "Prod")
else:
    sentry_client = None


class Price:
    """The base class for the prices in greed.
    Its int value is in minimum units, while its float and str values are in decimal format.int("""

    def __init__(self, value: typing.Union[int, float, str, "Price"], loc: localization.Localization):
        # Keep a reference to the localization file
        self.loc = loc
        if isinstance(value, int):
            # Keep the value as it is
            self.value = int(value)
        elif isinstance(value, float):
            # Convert the value to minimum units
            self.value = int(value * (10 ** int(config["Payments"]["currency_exp"])))
        elif isinstance(value, str):
            # Remove decimal points, then cast to int
            self.value = int(float(value.replace(",", ".")) * (10 ** int(config["Payments"]["currency_exp"])))
        elif isinstance(value, Price):
            # Copy self
            self.value = value.value

    def __repr__(self):
        return f"<Price of value {self.value}>"

    def __str__(self):
        return self.loc.get("currency_format_string",
                            symbol=config["Payments"]["currency_symbol"],
                            value="{0:.2f}".format(self.value / (10 ** int(config["Payments"]["currency_exp"]))))

    def __int__(self):
        return self.value

    def __float__(self):
        return self.value / (10 ** int(config["Payments"]["currency_exp"]))

    def __ge__(self, other):
        return self.value >= Price(other, self.loc).value

    def __le__(self, other):
        return self.value <= Price(other, self.loc).value

    def __eq__(self, other):
        return self.value == Price(other, self.loc).value

    def __gt__(self, other):
        return self.value > Price(other, self.loc).value

    def __lt__(self, other):
        return self.value < Price(other, self.loc).value

    def __add__(self, other):
        return Price(self.value + Price(other, self.loc).value, self.loc)

    def __sub__(self, other):
        return Price(self.value - Price(other, self.loc).value, self.loc)

    def __mul__(self, other):
        return Price(int(self.value * other), self.loc)

    def __floordiv__(self, other):
        return Price(int(self.value // other), self.loc)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return Price(Price(other, self.loc).value - self.value, self.loc)

    def __rmul__(self, other):

        return self.__mul__(other)

    def __iadd__(self, other):
        self.value += Price(other, self.loc).value
        return self

    def __isub__(self, other):
        self.value -= Price(other, self.loc).value
        return self

    def __imul__(self, other):
        self.value *= other
        self.value = int(self.value)
        return self

    def __ifloordiv__(self, other):
        self.value //= other
        return self


def telegram_html_escape(string: str):
    return string.replace("<", "&lt;") \
        .replace(">", "&gt;") \
        .replace("&", "&amp;") \
        .replace('"', "&quot;")


def catch_telegram_errors(func):
    """Decorator, can be applied to any function to retry in case of Telegram errors."""

    def result_func(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            # Bot was blocked by the user
            except telegram.error.Unauthorized:
                log.debug(f"Unauthorized to call {func.__name__}(), skipping.")
                break
            # Telegram API didn't answer in time
            except telegram.error.TimedOut:
                log.warning(f"Timed out while calling {func.__name__}(),"
                            f" retrying in {config['Telegram']['timed_out_pause']} secs...")
                time.sleep(int(config["Telegram"]["timed_out_pause"]))
            # Telegram is not reachable
            except telegram.error.NetworkError as error:
                log.error(f"Network error while calling {func.__name__}(),"
                          f" retrying in {config['Telegram']['error_pause']} secs...\n"
                          f"Full error: {error.message}")
                time.sleep(int(config["Telegram"]["error_pause"]))
            # Unknown error
            except telegram.error.TelegramError as error:
                if error.message.lower() in ["bad gateway", "invalid server response"]:
                    log.warning(f"Bad Gateway while calling {func.__name__}(),"
                                f" retrying in {config['Telegram']['error_pause']} secs...")
                    time.sleep(int(config["Telegram"]["error_pause"]))
                elif error.message.lower() == "timed out":
                    log.warning(f"Timed out while calling {func.__name__}(),"
                                f" retrying in {config['Telegram']['timed_out_pause']} secs...")
                    time.sleep(int(config["Telegram"]["timed_out_pause"]))
                else:
                    log.error(f"Telegram error while calling {func.__name__}(),"
                              f" retrying in {config['Telegram']['error_pause']} secs...\n"
                              f"Full error: {error.message}")
                    # Send the error to the Sentry server
                    if sentry_client is not None:
                        sentry_client.captureException(exc_info=sys.exc_info())
                    else:
                        traceback.print_exception(*sys.exc_info())
                    time.sleep(int(config["Telegram"]["error_pause"]))

    return result_func


class DuckBot:
    def __init__(self, *args, **kwargs):
        self.bot = telegram.Bot(*args, **kwargs)

    @catch_telegram_errors
    def send_message(self, *args, **kwargs):
        # All messages are sent in HTML parse mode
        return self.bot.send_message(parse_mode="HTML", *args, **kwargs)

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

    @catch_telegram_errors
    def send_message_markdown(self, *args, **kwargs):
        # Send message in markdown parse mode
        return self.bot.send_message(parse_mode="Markdown", *args, **kwargs)
    
    # More methods can be added here
