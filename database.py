from sqlalchemy import create_engine, Column, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy import Integer, BigInteger, String, Numeric, Text
from sqlalchemy.orm import sessionmaker, relationship
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

# Create a Session class able to initialize database sessions
Session = sessionmaker()

# Define all the database tables using the sqlalchemy declarative base
class User(TableDeclarativeBase):
    """A Telegram user who used the bot at least once."""

    # Telegram data
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    username = Column(String)

    # Current wallet credit
    credit = Column(Integer, nullable=False)

    # Extra table parameters
    __tablename__ = "users"

    def __init__(self, telegram_chat: telegram.Chat, **kwargs):
        # Initialize the super
        super().__init__(**kwargs)
        # Get the data from telegram
        self.user_id = telegram_chat.id
        self.first_name = telegram_chat.first_name
        self.last_name = telegram_chat.last_name
        self.username = telegram_chat.username
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
    price = Column(Integer)
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
               f"<i>{strings.in_stock_format_string.format(quantity=self.stock) if self.stock is not None else ''}</i>\n" \
               f"{strings.currency_format_string.format(symbol=strings.currency_symbol, value=self.price)}"

    def __repr__(self):
        return f"<Product {self.name}>"

    # TODO: add get image (and set image?) method(s)


class Transaction(TableDeclarativeBase):
    """A greed wallet transaction.
    Wallet credit ISN'T calculated from these, but they can be used to recalculate it."""

    # The internal transaction ID
    transaction_id = Column(Integer, primary_key=True)
    # The user whose credit is affected by this transaction
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    user = relationship("User")
    # The value of this transaction. Can be both negative and positive.
    value = Column(Integer, nullable=False)
    # Extra notes on the transaction
    notes = Column(Text)

    # Payment provider
    provider = Column(String)
    # Transaction ID supplied by Telegram
    telegram_charge_id = Column(String)
    # Transaction ID supplied by the payment provider
    provider_charge_id = Column(String)
    # Extra transaction data, may be required by the payment provider in case of a dispute
    payment_name = Column(String)
    payment_phone = Column(String)
    payment_email = Column(String)

    # Order ID
    order_id = Column(Integer)

    # Extra table parameters
    __tablename__ = "transactions"
    __table_args__ = (UniqueConstraint("provider", "provider_charge_id"),)

    def __str__(self):
        """Return the correctly formatted transaction value"""
        # Add a plus symbol if the value is positive
        string = "+" if self.value > 0 else ""
        # Add the correctly formatted value
        string += strings.currency_format_string.format(symbol=strings.currency_symbol, value=self.value)
        # Return the created string
        return string

    def __repr__(self):
        return f"<Transaction {self.transaction_id} - User {self.user_id} {str(self)}>"


class Admin(TableDeclarativeBase):
    """A greed administrator with his permissions."""

    # The telegram id
    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)
    user = relationship("User")
    # Permissions
    # TODO: unfinished

    # Extra table parameters
    __tablename__ = "admins"

    def __repr__(self):
        return f"<Admin {self.user_id}>"


# If this script is ran as main, try to create all the tables in the database
if __name__ == "__main__":
    TableDeclarativeBase.metadata.create_all()