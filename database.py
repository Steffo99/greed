from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, composite
from sqlalchemy import Column, BigInteger, Integer, String, Numeric, DateTime, ForeignKey, Float, create_engine
from dbcomposites import Coordinates

# Init the sqlalchemy engine
engine = create_engine("postgres://steffo:HIDDENPASSWORD@royal.steffo.eu:5432/pizzadev")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

# Create a new default session
session = Session()


class TelegramUser(Base):
    """Basic Telegram user data"""
    __tablename__ = "tusers"

    tid = Column(BigInteger, primary_key=True)
    tusername = Column(String)
    tfirstname = Column(String, nullable=False)
    tlastname = Column(String)

    def __str__(self):
        if self.tusername is not None:
            return f"@{self.tusername}"
        elif self.tlastname is not None:
            return f"{self.tfirstname} {self.tlastname}"
        else:
            return f"{self.tfirstname}"

    def __repr__(self):
        return f"<User #{self.tid}>"


class Pizza(Base):
    """Data for a pizza type"""
    __tablename__ = "pizza"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    details = Column(String)
    price = Column(Numeric, scale=2, nullable=False)

    def __str__(self, full=False):
        if full:
            return f"{self.name} [{self.price}]\n{self.details}"
        return f"{self.name} [{self.price}]"

    def __repr__(self):
        return f"<Pizza #{self.id}>"


class PizzaSelection(Base):
    """Data for a single pizza placed in a order"""
    __tablename__ = "pizzaselection"

    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    pizza_id = Column(Integer, ForeignKey("pizza.id"), primary_key=True)
    pizza = relationship("Pizza")

    notes = Column(String)

    def __repr__(self):
        return "<PizzaSelection of Pizza #{self.pizza_id} in Order #{self.order_id}>"


class Order(Base):
    """Data for a pizza order"""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    creation_time = Column(DateTime, nullable=False)
    requested_time = Column(DateTime)
    delivery_time = Column(DateTime)
    completed_time = Column(DateTime)
    notes = Column(String)

    delivery_long = Column(Float, nullable=False)
    delivery_lat = Column(Float, nullable=False)
    delivery_location = composite(Coordinates, delivery_long, delivery_lat)

    user_id = Column(Integer, ForeignKey("tusers.id"))
    user = relationship("TelegramUser")

    pizzas = relationship("PizzaSelection")

    def __repr__(self):
        return f"<Order #{self.id}>"


# If run as script, create all the tables in the db
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)