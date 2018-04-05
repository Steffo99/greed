import telegram
import telegram.error
import time
from configloader import config
from strings import currency_format_string, currency_symbol
import typing

class Price:
    def __init__(self, value:typing.Union[int, float, str, "Price"]=0):
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
        return currency_format_string.format(symbol=currency_symbol, value="{0:.2f}".format(self.value / (10 ** int(config["Payments"]["currency_exp"]))))

    def __int__(self):
        return self.value

    def __float__(self):
        return self.value / (10 ** int(config["Payments"]["currency_exp"]))

    def __ge__(self, other):
        return self.value >= Price(other).value

    def __le__(self, other):
        return self.value <= Price(other).value

    def __eq__(self, other):
        return self.value == Price(other).value

    def __gt__(self, other):
        return self.value > Price(other).value

    def __lt__(self, other):
        return self.value < Price(other).value

    def __add__(self, other):
        return Price(self.value + Price(other).value)

    def __sub__(self, other):
        return Price(self.value - Price(other).value)

    def __mul__(self, other):
        return Price(int(self.value * other))

    def __floordiv__(self, other):
        return Price(int(self.value // other))

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return Price(Price(other).value - self.value)

    def __rmul__(self, other):

        return self.__mul__(other)

    def __iadd__(self, other):
        self.value += Price(other).value
        return self

    def __isub__(self, other):
        self.value -= Price(other).value
        return self

    def __imul__(self, other):
        self.value *= other
        self.value = int(self.value)
        return self

    def __ifloordiv__(self, other):
        self.value //= other
        return self


def catch_telegram_errors(func):
    """Decorator, can be applied to any function to retry in case of Telegram errors."""
    def result_func(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except telegram.error.Unauthorized:
                print(f"Unauthorized to call {func.__name__}(), skipping.")
                break
            except telegram.error.TimedOut:
                print(f"Timed out while calling {func.__name__}(), retrying in 1 sec...")
                time.sleep(1)
            except telegram.error.NetworkError:
                print(f"Network error while calling {func.__name__}(), retrying in 5 secs...")
                time.sleep(5)
            else:
                break
    return result_func


class DuckBot:
    def __init__(self, *args, **kwargs):
        self.bot = telegram.Bot(*args, **kwargs)

    @catch_telegram_errors
    def send_message(self, *args, **kwargs):
        self.bot.send_message(*args, **kwargs)

    @catch_telegram_errors
    def edit_message_text(self, *args, **kwargs):
        self.bot.edit_message_text(*args, **kwargs)

    @catch_telegram_errors
    def edit_message_caption(self, *args, **kwargs):
        self.bot.edit_message_caption(*args, **kwargs)

    @catch_telegram_errors
    def edit_message_reply_markup(self, *args, **kwargs):
        self.bot.edit_message_reply_markup(*args, **kwargs)

    @catch_telegram_errors
    def get_updates(self, *args, **kwargs):
        self.bot.get_updates(*args, **kwargs)

    @catch_telegram_errors
    def get_me(self, *args, **kwargs):
        self.bot.get_me(*args, **kwargs)

    @catch_telegram_errors
    def answer_callback_query(self, *args, **kwargs):
        self.bot.answer_callback_query(*args, **kwargs)

    @catch_telegram_errors
    def answer_pre_checkout_query(self, *args, **kwargs):
        self.bot.answer_pre_checkout_query(*args, **kwargs)

    @catch_telegram_errors
    def send_invoice(self, *args, **kwargs):
        self.bot.send_invoice(*args, **kwargs)

    @catch_telegram_errors
    def get_file(self, *args, **kwargs):
        self.bot.get_file(*args, **kwargs)

    @catch_telegram_errors
    def send_chat_action(self, *args, **kwargs):
        self.bot.send_chat_action(*args, **kwargs)

    # TODO: add more methods