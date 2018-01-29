import threading
import typing
import uuid
import telegram
import strings
import configloader
import sys
import queue as queuem
import database as db
import re

class StopSignal:
    """A data class that should be sent to the worker when the conversation has to be stopped abnormally."""

    def __init__(self, reason: str=""):
        self.reason = reason


class ChatWorker(threading.Thread):
    """A worker for a single conversation. A new one is created every time the /start command is sent."""

    def __init__(self, bot: telegram.Bot, chat: telegram.Chat, *args, **kwargs):
        # Initialize the thread
        super().__init__(name=f"ChatThread {chat.first_name}", *args, **kwargs)
        # Store the bot and chat info inside the class
        self.bot = bot
        self.chat = chat
        # Open a new database session
        self.session = db.Session()
        # Get the user db data from the users and admin tables
        self.user = None
        self.admin = None
        # The sending pipe is stored in the ChatWorker class, allowing the forwarding of messages to the chat process
        self.queue = queuem.Queue()
        # The current active invoice payload; reject all invoices with a different payload
        self.invoice_payload = None

    def run(self):
        """The conversation code."""
        # TODO: catch all the possible exceptions
        # Welcome the user to the bot
        self.bot.send_message(self.chat.id, strings.conversation_after_start)
        # Get the user db data from the users and admin tables
        self.user = self.session.query(db.User).filter(db.User.user_id == self.chat.id).one_or_none()
        self.admin = self.session.query(db.Admin).filter(db.Admin.user_id == self.chat.id).one_or_none()
        # If the user isn't registered, create a new record and add it to the db
        if self.user is None:
            # Create the new record
            self.user = db.User(self.chat)
            # Add the new record to the db
            self.session.add(self.user)
            # Commit the transaction
            self.session.commit()
        # If the user is not an admin, send him to the user menu
        if self.admin is None:
            self.__user_menu()
        # If the user is an admin, send him to the admin menu
        else:
            self.__admin_menu()

    def stop(self, reason: str=""):
        """Gracefully stop the worker process"""
        # Send a stop message to the thread
        self.queue.put(StopSignal(reason))
        # Wait for the thread to stop
        self.join()

    def __receive_next_update(self) -> telegram.Update:
        """Get the next update from the queue.
        If no update is found, block the process until one is received.
        If a stop signal is sent, try to gracefully stop the thread."""
        # Pop data from the queue
        try:
            data = self.queue.get(timeout=int(configloader.config["Telegram"]["conversation_timeout"]))
        except queuem.Empty:
            # If the conversation times out, gracefully stop the thread
            self.__graceful_stop()
        # Check if the data is a stop signal instance
        if isinstance(data, StopSignal):
            # Gracefully stop the process
            self.__graceful_stop()
        # Return the received update
        return data

    def __wait_for_specific_message(self, items:typing.List[str]) -> str:
        """Continue getting updates until until one of the strings contained in the list is received as a message."""
        while True:
            # Get the next update
            update = self.__receive_next_update()
            # Ensure the update contains a message
            if update.message is None:
                continue
            # Ensure the message contains text
            if update.message.text is None:
                continue
            # Check if the message is contained in the list
            if update.message.text not in items:
                continue
            # Return the message text
            return update.message.text

    def __wait_for_regex(self, regex:str) -> str:
        """Continue getting updates until the regex finds a match in a message, then return the first capture group."""
        while True:
            # Get the next update
            update = self.__receive_next_update()
            # Ensure the update contains a message
            if update.message is None:
                continue
            # Ensure the message contains text
            if update.message.text is None:
                continue
            # Try to match the regex with the received message
            match = re.search(regex, update.message.text)
            # Ensure there is a match
            if match is None:
                continue
            # Return the first capture group
            return match.group(1)

    def __wait_for_precheckoutquery(self) -> telegram.PreCheckoutQuery:
        """Continue getting updates until a precheckoutquery is received.
        The payload is checked by the core before forwarding the message."""
        while True:
            # Get the next update
            update = self.__receive_next_update()
            # Ensure the update contains a precheckoutquery
            if update.pre_checkout_query is None:
                continue
            # Return the precheckoutquery
            return update.pre_checkout_query

    def __wait_for_successfulpayment(self) -> telegram.SuccessfulPayment:
        """Continue getting updates until a successfulpayment is received."""
        while True:
            # Get the next update
            update = self.__receive_next_update()
            # Ensure the update contains a message
            if update.message is None:
                continue
            # Ensure the message is a successfulpayment
            if update.message.successful_payment is None:
                continue
            # Return the successfulpayment
            return update.message.successful_payment

    def __user_menu(self):
        """Function called from the run method when the user is not an administrator.
        Normal bot actions should be placed here."""
        # Loop used to returning to the menu after executing a command
        while True:
            # Create a keyboard with the user main menu
            keyboard = [[telegram.KeyboardButton(strings.menu_order)],
                        [telegram.KeyboardButton(strings.menu_order_status)],
                        [telegram.KeyboardButton(strings.menu_add_credit)],
                        [telegram.KeyboardButton(strings.menu_bot_info)]]
            # Send the previously created keyboard to the user (ensuring it can be clicked only 1 time)
            self.bot.send_message(self.chat.id, strings.conversation_open_user_menu,
                                  reply_markup=telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
            # Wait for a reply from the user
            selection = self.__wait_for_specific_message([strings.menu_order, strings.menu_order_status,
                                                          strings.menu_add_credit, strings.menu_bot_info])
            # If the user has selected the Order option...
            if selection == strings.menu_order:
                # Open the order menu
                self.__order_menu()
            # If the user has selected the Order Status option...
            elif selection == strings.menu_order_status:
                # Display the order(s) status
                self.__order_status()
            # If the user has selected the Add Credit option...
            elif selection == strings.menu_add_credit:
                # Display the add credit menu
                self.__add_credit_menu()
            # If the user has selected the Bot Info option...
            elif selection == strings.menu_bot_info:
                # Display information about the bot
                self.__bot_info()

    def __order_menu(self):
        raise NotImplementedError()

    def __order_status(self):
        raise NotImplementedError()

    def __add_credit_menu(self):
        """Add more credit to the account."""
        # TODO: a loop might be needed here
        # Create a payment methods keyboard
        keyboard = list()
        # Add the supported payment methods to the keyboard
        # Cash
        keyboard.append([telegram.KeyboardButton(strings.menu_cash)])
        # Telegram Payments
        if configloader.config["Credit Card"]["credit_card_token"] != "":
            keyboard.append([telegram.KeyboardButton(strings.menu_credit_card)])
        # Keyboard: go back to the previous menu
        keyboard.append([telegram.KeyboardButton(strings.menu_cancel)])
        # Send the keyboard to the user
        self.bot.send_message(self.chat.id, strings.conversation_payment_method,
                              reply_markup=telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        # Wait for a reply from the user
        selection = self.__wait_for_specific_message([strings.menu_cash, strings.menu_credit_card, strings.menu_cancel])
        # If the user has selected the Cash option...
        if selection == strings.menu_cash:
            # Go to the pay with cash function
            self.__add_credit_cash()
        # If the user has selected the Credit Card option...
        elif selection == strings.menu_credit_card:
            # Go to the pay with credit card function
            self.__add_credit_cc()
        # If the user has selected the Cancel option...
        elif selection == strings.menu_add_credit:
            # Send him back to the previous menu
            return

    def __add_credit_cash(self):
        """Tell the user how to pay with cash at this shop."""
        self.bot.send_message(self.chat.id, strings.payment_cash)

    def __add_credit_cc(self):
        """Add money to the wallet through a credit card payment."""
        # Create a keyboard to be sent later
        keyboard = [[telegram.KeyboardButton(strings.currency_format_string.format(symbol=strings.currency_symbol, value="10"))],
                    [telegram.KeyboardButton(strings.currency_format_string.format(symbol=strings.currency_symbol, value="25"))],
                    [telegram.KeyboardButton(strings.currency_format_string.format(symbol=strings.currency_symbol, value="50"))],
                    [telegram.KeyboardButton(strings.currency_format_string.format(symbol=strings.currency_symbol, value="100"))]]
        # Loop used to continue asking if there's an error during the input
        while True:
            # Send the message and the keyboard
            self.bot.send_message(self.chat.id, strings.payment_cc_amount,
                                  reply_markup=telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
            # Wait until a valid amount is sent
            # TODO: check and debug the regex
            selection = int(self.__wait_for_regex(r"([0-9]{1,3}(?:[.,][0-9]{1,2})?)").replace(".", "").replace(",", "")) * (10 ** int(configloader.config["Payments"]["currency_exp"]))
            # Ensure the amount is within the range
            if selection > int(configloader.config["Payments"]["max_amount"]):
                self.bot.send_message(self.chat.id, strings.error_payment_amount_over_max.format(max_amount=strings.currency_format_string.format(symbol=strings.currency_symbol, value=configloader.config["Payments"]["max_amount"])))
                continue
            elif selection < int(configloader.config["Payments"]["min_amount"]):
                self.bot.send_message(self.chat.id, strings.error_payment_amount_under_min.format(min_amount=strings.currency_format_string.format(symbol=strings.currency_symbol, value=configloader.config["Payments"]["min_amount"])))
                continue
            break
        # Set the invoice active invoice payload
        self.invoice_payload = str(uuid.uuid4())
        # Create the price array
        prices = [telegram.LabeledPrice(label=strings.payment_invoice_label, amount=selection)]
        # If the user has to pay a fee when using the credit card, add it to the prices list
        fee_percentage = float(configloader.config["Credit Card"]["fee_percentage"]) / 100
        fee_fixed = int(configloader.config["Credit Card"]["fee_fixed"])
        total_fee = int(selection * fee_percentage) + fee_fixed
        if total_fee > 0:
            prices.append(telegram.LabeledPrice(label=strings.payment_invoice_fee_label, amount=int(total_fee)))
        else:
            # Otherwise, set the fee to 0 to ensure no accidental discounts are applied
            total_fee = 0
        # The amount is valid, send the invoice
        self.bot.send_invoice(self.chat.id,
                              title=strings.payment_invoice_title,
                              description=strings.payment_invoice_description.format(amount=strings.currency_format_string.format(symbol=strings.currency_symbol, value=selection / (10 ** int(configloader.config["Payments"]["currency_exp"])))),
                              payload=self.invoice_payload,
                              provider_token=configloader.config["Credit Card"]["credit_card_token"],
                              start_parameter="tempdeeplink",  # TODO: no idea on how deeplinks should work
                              currency=configloader.config["Payments"]["currency"],
                              prices=prices,
                              need_name=configloader.config["Credit Card"]["name_required"] == "yes",
                              need_email=configloader.config["Credit Card"]["email_required"] == "yes",
                              need_phone_number=configloader.config["Credit Card"]["phone_required"] == "yes")
        # Wait for the invoice
        precheckoutquery = self.__wait_for_precheckoutquery()
        # TODO: ensure the bot doesn't die here!
        # Accept the checkout
        self.bot.answer_pre_checkout_query(precheckoutquery.id, ok=True)
        # Wait for the payment
        successfulpayment = self.__wait_for_successfulpayment()
        # Create a new database transaction
        transaction = db.Transaction(user=self.user,
                                     value=successfulpayment.total_amount - int(total_fee),
                                     provider="Credit Card",
                                     telegram_charge_id=successfulpayment.telegram_payment_charge_id,
                                     provider_charge_id=successfulpayment.provider_payment_charge_id)
        if successfulpayment.order_info is not None:
            transaction.payment_name = successfulpayment.order_info.name
            transaction.payment_email = successfulpayment.order_info.email
            transaction.payment_phone = successfulpayment.order_info.phone_number
        # Add the credit to the user account
        self.user.credit += successfulpayment.total_amount - total_fee
        # Add and commit the transaction
        self.session.add(transaction)
        self.session.commit()

    def __bot_info(self):
        """Send information about the bot."""
        self.bot.send_message(self.chat.id, strings.bot_info, parse_mode="HTML")

    def __admin_menu(self):
        """Function called from the run method when the user is an administrator.
        Administrative bot actions should be placed here."""
        # Loop used to return to the menu after executing a command
        while True:
            # Create a keyboard with the admin main menu
            keyboard = [[telegram.KeyboardButton(strings.menu_products)],
                        [telegram.KeyboardButton(strings.menu_orders)],
                        [telegram.KeyboardButton(strings.menu_user_mode)]]
            # Send the previously created keyboard to the user (ensuring it can be clicked only 1 time)
            self.bot.send_message(self.chat.id, strings.conversation_open_admin_menu,
                                  reply_markup=telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
            # Wait for a reply from the user
            selection = self.__wait_for_specific_message([strings.menu_products, strings.menu_orders,
                                                          strings.menu_user_mode])
            # If the user has selected the Products option...
            if selection == strings.menu_products:
                # Open the products menu
                self.__products_menu()
            # If the user has selected the Orders option...
            elif selection == strings.menu_orders:
                # Open the orders menu
                self.__orders_menu()
            # If the user has selected the User mode option...
            elif selection == strings.menu_user_mode:
                # Start the bot in user mode
                self.__user_menu()

    def __products_menu(self):
        """Display the admin menu to select a product to edit."""
        # Get the products list from the db
        products = self.session.query(db.Product).all()
        # Create a list of product names
        product_names = [product.name for product in products]
        # Insert at the start of the list the add product option
        product_names.insert(0, strings.menu_add_product)
        # Create a keyboard using the product names
        keyboard = [[telegram.KeyboardButton(product_name)] for product_name in product_names]
        # Send the previously created keyboard to the user (ensuring it can be clicked only 1 time)
        self.bot.send_message(self.chat.id, strings.conversation_admin_select_product,
                              reply_markup=telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        # Wait for a reply from the user
        selection = self.__wait_for_specific_message(product_names)
        # If the user has selected the Add Product option...
        if selection == strings.menu_add_product:
            # Open the add product menu
            self.__add_product_menu()
        # If the user has selected a product
        else:
            # Open the edit menu for that specific product
            self.__edit_product_menu(selection)

    def __add_product_menu(self):
        """Add a product to the database."""
        # Ask for the product name until a valid product name is specified
        while True:
            # Ask the question to the user
            self.bot.send_message(self.chat.id, strings.ask_product_name)
            # Wait for an answer
            name = self.__wait_for_regex(r"(.*)")
            # Ensure a product with that name doesn't already exist
            if self.session.query(db.Product).filter_by(name=name).one_or_none() is None:
                # Exit the loop
                break
            self.bot.send_message(self.chat.id, strings.error_duplicate_name)
        # Ask for the product description
        self.bot.send_message(self.chat.id, strings.ask_product_description)
        # Wait for an answer
        description = self.__wait_for_regex(r"(.*)")
        # Ask for the product price
        self.bot.send_message(self.chat.id, strings.ask_product_price)
        # Wait for an answer
        price = int(self.__wait_for_regex(r"([0-9]{1,3}(?:[.,][0-9]{1,2})?)").replace(".", "").replace(",", "")) * (
                    10 ** int(configloader.config["Payments"]["currency_exp"]))
        # TODO: ask for product image
        # Create the db record for the product
        product = db.Product(name=name,
                             description=description,
                             price=price)
        # Add the record to the session, then commit
        self.session.add(product)
        self.session.commit()
        # Notify the user
        self.bot.send_message(self.chat.id, strings.success_product_added)

    def __edit_product_menu(self, name: str):
        raise NotImplementedError()

    def __orders_menu(self):
        raise NotImplementedError()

    def __graceful_stop(self):
        """Handle the graceful stop of the thread."""
        # Notify the user that the session has expired and remove the keyboard
        self.bot.send_message(self.chat.id, strings.conversation_expired, reply_markup=telegram.ReplyKeyboardRemove())
        # Close the database session
        # End the process
        sys.exit(0)
