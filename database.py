from sqlalchemy import create_engine, Column, ForeignKey, UniqueConstraint
from sqlalchemy import Integer, BigInteger, String, Text, LargeBinary, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import configloader
import telegram
import strings
import requests
from html import escape
from utils import Price

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
        self.credit = 0

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

    # Product id
    id = Column(Integer, primary_key=True)
    # Product name
    name = Column(String)
    # Product description
    description = Column(Text)
    # Product price, if null product is not for sale
    price = Column(Integer)
    # Image data
    image = Column(LargeBinary)
    # Product has been deleted
    deleted = Column(Boolean, nullable=False)
    # Stock quantity, if null product has infinite stock
    stock = Column(Integer)

    # Extra table parameters
    __tablename__ = "products"

    # No __init__ is needed, the default one is sufficient

    def __str__(self):
        return self.text()

    def text(self, style:str="full", cart_qty:int=None):
        """Return the product details formatted with Telegram HTML. The image is omitted."""
        if style == "short":
            return f"{cart_qty}x {escape(self.name)} - {str(Price(self.price) * cart_qty)}"
        elif style == "full":
            return f"<b>{escape(self.name)}</b>\n" \
                   f"{escape(self.description)}\n" \
                   f"<i>{strings.in_stock_format_string.format(quantity=self.stock) if self.stock is not None else ''}</i>\n" \
                   f"{str(Price(self.price))}\n" \
                   f"<b>{strings.in_cart_format_string.format(quantity=cart_qty) if cart_qty is not None else ''}</b>"
        elif style == "image":
            return f"{escape(self.name)}\n" \
                   f"{escape(self.description)}\n" \
                   f"{strings.in_stock_format_string.format(quantity=self.stock) if self.stock is not None else ''}\n" \
                   f"{str(Price(self.price))}\n" \
                   f"{strings.in_cart_format_string.format(quantity=cart_qty) if cart_qty is not None else ''}"
        else:
            raise ValueError("style is not an accepted value")

    def __repr__(self):
        return f"<Product {self.name}>"

    def send_as_message(self, chat_id: int) -> dict:
        """Send a message containing the product data."""
        if self.image is None:
            r = requests.get(f"https://api.telegram.org/bot{configloader.config['Telegram']['token']}/sendMessage",
                           params={"chat_id": chat_id,
                                   "text": self.text(),
                                   "parse_mode": "HTML"})
        else:
            r = requests.post(f"https://api.telegram.org/bot{configloader.config['Telegram']['token']}/sendPhoto",
                              files={"photo": self.image},
                              params={"chat_id": chat_id,
                                      "caption": self.text(style="image"),
                                      "parse_mode": "HTML"})
        return r.json()

    def set_image(self, file: telegram.File):
        """Download an image from Telegram and store it in the image column.
        This is a slow blocking function. Try to avoid calling it directly, use a thread if possible."""
        # Download the photo through a get request
        r = requests.get(file.file_path)
        # Store the photo in the database record
        self.image = r.content


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
        return f"<Transaction {self.transaction_id} for User {self.user_id} {str(self)}>"


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


class Order(TableDeclarativeBase):
    """An order which has been placed by an user.
    It may include multiple products, available in the OrderItem table."""

    # The unique order id
    order_id = Column(Integer, primary_key=True)
    # The user who placed the order
    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    user = relationship("User")
    # Date of creation
    creation_date = Column(DateTime, nullable=False)
    # Date of delivery, None if the item hasn't been delivered yet
    delivery_date = Column(DateTime)
    # List of items in the order
    items = relationship("OrderItem")
    # Extra details specified by the purchasing user
    notes = Column(Text)

    # Extra table parameters
    __tablename__ = "orders"

    def __repr__(self):
        return f"<Order {self.order_id} placed by User {self.user_id}>"


class OrderItem(TableDeclarativeBase):
    """A product that has been purchased as part of an order."""

    # The unique item id
    item_id = Column(Integer, primary_key=True)
    # The product that is being ordered
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product")
    # The order in which this item is being purchased
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)

    # Extra table parameters
    __tablename__ = "orderitems"

    def __repr__(self):
        return f"<OrderItem {self.item_id}>"


# If this script is ran as main, try to create all the tables in the database
if __name__ == "__main__":
    TableDeclarativeBase.metadata.create_all()