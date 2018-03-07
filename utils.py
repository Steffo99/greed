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
        return Price(self.value * Price(other).value)

    def __floordiv__(self, other):
        return Price(self.value // Price(other).value)

    def __radd__(self, other):
        self.__add__(other)

    def __rsub__(self, other):
        return Price(Price(other).value - self.value)

    def __rmul__(self, other):
        self.__mul__(other)

    def __iadd__(self, other):
        self.value += Price(other).value
        return self

    def __isub__(self, other):
        self.value -= Price(other).value
        return self

    def __imul__(self, other):
        self.value *= Price(other).value
        return self

    def __ifloordiv__(self, other):
        self.value //= Price(other).value
        return self
