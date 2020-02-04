import typing
from sqlalchemy import create_engine, Column, ForeignKey, UniqueConstraint
from sqlalchemy import Integer, BigInteger, String, Text, LargeBinary, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import configloader
import telegram
import requests
import utils
import importlib

language = configloader.config["Config"]["language"]
strings = importlib.import_module("strings." + language)

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

    def identifiable_str(self):
        """Describe the user in the best way possible, ensuring a way back to the database record exists."""
        return f"user_{self.user_id} ({str(self)})"

    def mention(self):
        """Mention the user in the best way possible given the available data."""
        if self.username is not None:
            return f"@{self.username}"
        else:
            return f"[{self.first_name}](tg://user?id={self.user_id})"

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

    # Extra table parameters
    __tablename__ = "products"

    # No __init__ is needed, the default one is sufficient

    def __str__(self):
        return self.text()

    def text(self, style: str="full", cart_qty: int=None):
        """Return the product details formatted with Telegram HTML. The image is omitted."""
        if style == "short":
            return f"{cart_qty}x {utils.telegram_html_escape(self.name)} - {str(utils.Price(self.price) * cart_qty)}"
        elif style == "full":
            if cart_qty is not None:
                cart = strings.in_cart_format_string.format(quantity=cart_qty)
            else:
                cart = ''
            return strings.product_format_string.format(name=utils.telegram_html_escape(self.name),
                                                        description=utils.telegram_html_escape(self.description),
                                                        price=str(utils.Price(self.price)),
                                                        cart=cart)
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
                                      "caption": self.text(),
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
    # TODO: split this into multiple tables

    # The internal transaction ID
    transaction_id = Column(Integer, primary_key=True)
    # The user whose credit is affected by this transaction
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    user = relationship("User")
    # The value of this transaction. Can be both negative and positive.
    value = Column(Integer, nullable=False)
    # Refunded status: if True, ignore the value of this transaction when recalculating
    refunded = Column(Boolean, default=False)
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
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    order = relationship("Order")

    # Extra table parameters
    __tablename__ = "transactions"
    __table_args__ = (UniqueConstraint("provider", "provider_charge_id"),)

    def __str__(self):
        string = f"<b>T{self.transaction_id}</b> | {str(self.user)} | {utils.Price(self.value)}"
        if self.refunded:
            string += f" | {strings.emoji_refunded}"
        if self.provider:
            string += f" | {self.provider}"
        if self.notes:
            string += f" | {self.notes}"
        return string

    def __repr__(self):
        return f"<Transaction {self.transaction_id} for User {self.user_id} {str(self)}>"


class Admin(TableDeclarativeBase):
    """A greed administrator with his permissions."""

    # The telegram id
    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)
    user = relationship("User")
    # Permissions
    edit_products = Column(Boolean, default=False)
    receive_orders = Column(Boolean, default=False)
    create_transactions = Column(Boolean, default=False)
    display_on_help = Column(Boolean, default=False)
    is_owner = Column(Boolean, default=False)
    # Live mode enabled
    live_mode = Column(Boolean, default=False)

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
    # Date of delivery
    delivery_date = Column(DateTime)
    # Date of refund: if null, product hasn't been refunded
    refund_date = Column(DateTime)
    # Refund reason: if null, product hasn't been refunded
    refund_reason = Column(Text)
    # List of items in the order
    items: typing.List["OrderItem"] = relationship("OrderItem")
    # Extra details specified by the purchasing user
    notes = Column(Text)
    # Linked transaction
    transaction = relationship("Transaction", uselist=False)

    # Extra table parameters
    __tablename__ = "orders"

    def __repr__(self):
        return f"<Order {self.order_id} placed by User {self.user_id}>"

    def get_text(self, session, user=False):
        joined_self = session.query(Order).filter_by(order_id=self.order_id).join(Transaction).one()
        items = ""
        for item in self.items:
            items += str(item) + "\n"
        if self.delivery_date is not None:
            status_emoji = strings.emoji_completed
            status_text = strings.text_completed
        elif self.refund_date is not None:
            status_emoji = strings.emoji_refunded
            status_text = strings.text_refunded
        else:
            status_emoji = strings.emoji_not_processed
            status_text = strings.text_not_processed
        if user and configloader.config["Appearance"]["full_order_info"] == "no":
            return strings.user_order_format_string.format(status_emoji=status_emoji,
                                                           status_text=status_text,
                                                           items=items,
                                                           notes=self.notes,
                                                           value=str(utils.Price(-joined_self.transaction.value))) + \
                (strings.refund_reason.format(reason=self.refund_reason) if self.refund_date is not None else "")
        else:
            return status_emoji + " " + \
                strings.order_number.format(id=self.order_id) + "\n" + \
                strings.order_format_string.format(user=self.user.mention(),
                                                   date=self.creation_date.isoformat(),
                                                   items=items,
                                                   notes=self.notes if self.notes is not None else "",
                                                   value=str(utils.Price(-joined_self.transaction.value))) + \
                (strings.refund_reason.format(reason=self.refund_reason) if self.refund_date is not None else "")


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

    def __str__(self):
        return f"{self.product.name} - {str(utils.Price(self.product.price))}"

    def __repr__(self):
        return f"<OrderItem {self.item_id}>"


TableDeclarativeBase.metadata.create_all()
