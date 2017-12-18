from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy import Integer, BigInteger, String, Numeric, Text
from sqlalchemy.ext.declarative import declarative_base
import configloader
import telegram
import decimal
import strings
from html import escape

# Create a (lazy) database engine
engine = create_engine(configloader.config["Database"]["engine"])

# Create a base class to define all the database subclasses
TableDeclarativeBase = declarative_base(bind=engine)

# Define all the database tables using the sqlalchemy declarative base
class User(TableDeclarativeBase):
    """A Telegram user who used the bot at least once."""

    # Telegram data
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    username = Column(String)

    # Current wallet credit
    credit = Column(Numeric, nullable=False)

    # Extra table parameters
    __tablename__ = "users"

    def __init__(self, telegram_user: telegram.User):
        # Get the data from telegram
        self.id = telegram_user.id
        self.first_name = telegram_user.first_name
        self.last_name = telegram_user.last_name
        self.username = telegram_user.username
        # The starting wallet value is 0
        self.credit = decimal.Decimal("0")

    def __str__(self):
        """Describe the user in the best way possible given the available data."""
        if self.username is not None:
            return f"@{self.username}"
        elif self.last_name is not None:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.first_name

    def __repr__(self):
        return f"<User {self} having {self.credit} credit>"


class Product(TableDeclarativeBase):
    """A purchasable product."""

    # Product name
    name = Column(String, primary_key=True)
    # Product description
    description = Column(Text)
    # Product price, if null product is not for sale
    price = Column(Numeric)
    # Image filename
    image = Column(String)
    # Stock quantity, if null product has infinite stock
    stock = Column(Integer)

    # Extra table parameters
    __tablename__ = "product"

    # No __init__ is needed, the default one is sufficient

    def __str__(self):
        """Return the product details formatted with Telegram HTML. The image is omitted."""
        return f"<b>{escape(self.name)}</b>\n" \
               f"{escape(self.description)}\n" \
               f"<i>{format(strings.in_stock_format_string, quantity=self.stock) if self.stock is not None else ''}</i>\n" \
               f"{format(strings.currency_format_string, symbol=strings.currency_symbol, value=self.price)}"

    def __repr__(self):
        return f"<Product {self.name}>"

    # TODO: add get image (and set image?) method(s)


class Transactions(TableDeclarativeBase):
    """A greed wallet transaction.
    Wallet credit ISN'T calculated from these, but they can be used to recalculate it."""

    # The internal transaction ID
    transaction_id = Column(BigInteger, primary_key=True)
    # The user whose credit is affected by this transaction
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    # The value of this transaction. Can be both negative and positive.
    value = Column(Numeric, nullable=False)
    # Extra notes on the transaction
    notes = Column(Text)

    # TODO: there still are some missing fields