import telegram
import telegram.error
import time
from strings import currency_format_string, currency_symbol
import typing
import sys
import strings


class Price:
    """The base class for the prices in greed.
    Its int value is in minimum units, while its float and str values are in decimal format.int("""
    def __init__(self, value: typing.Union[int, float, str, "Price"], exp: int):
        if isinstance(value, int):
            # Keep the value as it is
            self.value = int(value)
        elif isinstance(value, float):
            # Convert the value to minimum units
            self.value = int(value * (10 ** exp))
        elif isinstance(value, str):
            # Remove decimal points, then cast to int
            self.value = int(float(value.replace(",", ".")) * (10 ** exp))
        elif isinstance(value, Price):
            # Copy self
            self.value = value.value
        else:
            raise TypeError("Value is of an unsupported type")
        self.exp: int = exp

    def __repr__(self):
        return f"<Price of value {self.value}>"

    def __str__(self):
        return currency_format_string.format(symbol=currency_symbol,
                                             value="{0:.2f}".format(
                                                 self.value / (10 ** self.exp)))

    def __int__(self):
        return self.value

    def __float__(self):
        return self.value / (10 ** self.exp)

    def __ge__(self, other):
        # Assuming currency exp is the same for the compared prices
        return self.value >= Price(other, self.exp).value

    def __le__(self, other):
        # Assuming currency exp is the same for the compared prices
        return self.value <= Price(other, self.exp).value

    def __eq__(self, other):
        # Assuming currency exp is the same for the compared prices
        return self.value == Price(other, self.exp).value

    def __gt__(self, other):
        # Assuming currency exp is the same for the compared prices
        return self.value > Price(other, self.exp).value

    def __lt__(self, other):
        # Assuming currency exp is the same for the compared prices
        return self.value < Price(other, self.exp).value

    def __add__(self, other):
        # Assuming currency exp is the same for the compared prices
        return Price(self.value + Price(other, self.exp).value, self.exp)

    def __sub__(self, other):
        # Assuming currency exp is the same for the compared prices
        return Price(self.value - Price(other, self.exp).value, self.exp)

    def __mul__(self, other):
        # Assuming currency exp is the same for the compared prices
        return Price(int(self.value * other), self.exp)

    def __floordiv__(self, other):
        # Assuming currency exp is the same for the compared prices
        return Price(int(self.value // other), self.exp)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        # Assuming currency exp is the same for the compared prices
        return Price(Price(other, self.exp).value - self.value, self.exp)

    def __rmul__(self, other):

        return self.__mul__(other)

    def __iadd__(self, other):
        # Assuming currency exp is the same for the compared prices
        self.value += Price(other, self.exp).value
        return self

    def __isub__(self, other):
        # Assuming currency exp is the same for the compared prices
        self.value -= Price(other, self.exp).value
        return self

    def __imul__(self, other):
        self.value *= other
        self.value = int(self.value)
        return self

    def __ifloordiv__(self, other):
        self.value //= other
        return self


def telegram_html_escape(string: str):
    return string.replace("<", "&lt;")\
                 .replace(">", "&gt;")\
                 .replace("&", "&amp;")\
                 .replace('"', "&quot;")


def catch_telegram_errors(func):
    """Decorator, can be applied to any function to retry in case of Telegram errors."""
    def result_func(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            # Bot was blocked by the user
            except telegram.error.Unauthorized:
                print(f"Unauthorized to call {func.__name__}(), skipping.")
                break
            # Telegram API didn't answer in time
            except telegram.error.TimedOut:
                print(f"Timed out while calling {func.__name__}(),"
                      f" retrying in {config['Telegram']['timed_out_pause']} secs...")
                time.sleep(int(config["Telegram"]["timed_out_pause"]))
            # Telegram is not reachable
            except telegram.error.NetworkError as error:
                print(f"Network error while calling {func.__name__}(),"
                      f" retrying in {config['Telegram']['error_pause']} secs...")
                # Display the full NetworkError if in debug mode
                if __debug__:
                    print(f"Full error: {error.message}")
                time.sleep(int(config["Telegram"]["error_pause"]))
            # Unknown error
            except telegram.error.TelegramError as error:
                if error.message.lower() in ["bad gateway", "invalid server response"]:
                    print(f"Bad Gateway while calling {func.__name__}(),"
                          f" retrying in {config['Telegram']['error_pause']} secs...")
                    time.sleep(int(config["Telegram"]["error_pause"]))
                elif error.message.lower() == "timed out":
                    print(f"Timed out while calling {func.__name__}(),"
                          f" retrying in {config['Telegram']['timed_out_pause']} secs...")
                    time.sleep(int(config["Telegram"]["timed_out_pause"]))
                else:
                    print(f"Telegram error while calling {func.__name__}(),"
                          f" retrying in {config['Telegram']['error_pause']} secs...")
                    # Display the full TelegramError if in debug mode
                    if __debug__:
                        print(f"Full error: {error.message}")
                    # Send the error to the Sentry server
                    elif sentry_client is not None:
                        sentry_client.captureException(exc_info=sys.exc_info())
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

    # More methods can be added here


def boolmoji(boolean: bool):
    return strings.emoji_yes if boolean else strings.emoji_no
