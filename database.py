from sqlalchemy import Table, Column, BigInteger, Numeric, String, Text, MetaData, ForeignKey
import decimal

# Create a metadata object containing info about the tables in the database
metadata = MetaData()

# Metadata for the users table
# TODO: maybe add a 'credit' column
users = Table("users", metadata,
              Column("telegram_user_id", BigInteger, primary_key=True),
              Column("first_name", String, nullable=False),
              Column("last_name", String),
              Column("username", String))

# Metadata for the admins table
# TODO: add columns for all the possible permissions
admins = Table("admins", metadata,
               Column("telegram_user_id", ForeignKey("users.telegram_user_id"), primary_key=True))

# Metadata for the products table
products = Table("products", metadata,
                 Column("product_name", String, primary_key=True),
                 Column("description", Text),
                 Column("price", Numeric(...)))

#TODO: many things are still missing...
raise NotImplementedError()