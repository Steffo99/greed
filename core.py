import sys
import telegram
import strings
import worker
import configloader
import utils
import threading
import flask
from blockonomics import Blockonomics
import database as db
import datetime

def main():
    """The core code of the program. Should be run only in the main process!"""

    # Rename the main thread for presentation purposes
    threading.current_thread().name = "Core"

    # Create a bot instance
    bot = utils.DuckBot(configloader.config["Telegram"]["token"])

    # Test the specified token
    try:
        bot.get_me()
    except telegram.error.Unauthorized:
        print("The token you have entered in the config file is invalid.\n"
              "Fix it, then restart this script.")
        sys.exit(1)

    # Create a dictionary linking the chat ids to the ChatWorker objects
    # {"1234": <ChatWorker>}
    chat_workers = {}

    # Current update offset; if None it will get the last 100 unparsed messages
    next_update = None

    # Notify on the console that the bot is starting
    print("greed-bot is now starting!")

    # Main loop of the program
    while True:
        # Get a new batch of 100 updates and mark the last 100 parsed as read
        updates = bot.get_updates(offset=next_update,
                                  timeout=int(configloader.config["Telegram"]["long_polling_timeout"]))
        # Parse all the updates
        for update in updates:
            # If the update is a message...
            if update.message is not None:
                # Ensure the message has been sent in a private chat
                if update.message.chat.type != "private":
                    # Notify the chat
                    bot.send_message(update.message.chat.id, strings.error_nonprivate_chat)
                    # Skip the update
                    continue
                # If the message is a start command...
                if isinstance(update.message.text, str) and update.message.text == "/start":
                    # Check if a worker already exists for that chat
                    old_worker = chat_workers.get(update.message.chat.id)
                    # If it exists, gracefully stop the worker
                    if old_worker:
                        old_worker.stop("request")
                    # Initialize a new worker for the chat
                    new_worker = worker.ChatWorker(bot, update.message.chat)
                    # Start the worker
                    new_worker.start()
                    # Store the worker in the dictionary
                    chat_workers[update.message.chat.id] = new_worker
                    # Skip the update
                    continue
                # Otherwise, forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.message.chat.id)
                # Ensure a worker exists for the chat and is alive
                if receiving_worker is None or not receiving_worker.is_alive():
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.message.chat.id, strings.error_no_worker_for_chat,
                                     reply_markup=telegram.ReplyKeyboardRemove())
                    # Skip the update
                    continue
                # Forward the update to the worker
                receiving_worker.queue.put(update)
            # If the update is a inline keyboard press...
            if isinstance(update.callback_query, telegram.CallbackQuery):
                # Forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.callback_query.from_user.id)
                # Ensure a worker exists for the chat
                if receiving_worker is None:
                    # Suggest that the user restarts the chat with /start
                    bot.send_message(update.callback_query.from_user.id, strings.error_no_worker_for_chat)
                    # Skip the update
                    continue
                # Check if the pressed inline key is a cancel button
                if update.callback_query.data == "cmd_cancel":
                    # Forward a CancelSignal to the worker
                    receiving_worker.queue.put(worker.CancelSignal())
                    # Notify the Telegram client that the inline keyboard press has been received
                    bot.answer_callback_query(update.callback_query.id)
                else:
                    # Forward the update to the worker
                    receiving_worker.queue.put(update)
            # If the update is a precheckoutquery, ensure it hasn't expired before forwarding it
            if isinstance(update.pre_checkout_query, telegram.PreCheckoutQuery):
                # Forward the update to the corresponding worker
                receiving_worker = chat_workers.get(update.pre_checkout_query.from_user.id)
                # Check if it's the active invoice for this chat
                if receiving_worker is None or\
                        update.pre_checkout_query.invoice_payload != receiving_worker.invoice_payload:
                    # Notify the user that the invoice has expired
                    try:
                        bot.answer_pre_checkout_query(update.pre_checkout_query.id,
                                                      ok=False,
                                                      error_message=strings.error_invoice_expired)
                    except telegram.error.BadRequest:
                        print(f"ERROR: pre_checkout_query expired before an answer could be sent")
                    # Go to the next update
                    continue
                # Forward the update to the worker
                receiving_worker.queue.put(update)
        # If there were any updates...
        if len(updates):
            # Mark them as read by increasing the update_offset
            next_update = updates[-1].update_id + 1

# Start the bitcoin callback listener
app = flask.Flask(__name__)
@app.route('/callback', methods=['GET'])
def callback():
    network_confirmations = configloader.config["Bitcoin"]["network_confirmations"]
    # Fetch the callback parameters
    secret = flask.request.args.get("secret")
    status = int(flask.request.args.get("status"))
    address = flask.request.args.get("addr")
    # Check the status and secret
    if secret == configloader.config["Bitcoin"]["secret"]:
        # Fetch the current transaction by address
        dbsession = db.Session()
        transaction = dbsession.query(db.BtcTransaction).filter(db.BtcTransaction.address == address).one_or_none()
        if status >= network_confirmations:
            if transaction.txid == "":
                # Check timestamp
                # If timeout period has past update and use new btc price
                current_time = datetime.datetime.now()
                timeout = 30
                print (transaction)
                if current_time - datetime.timedelta(minutes = timeout) > datetime.datetime.strptime(transaction.timestamp, '%Y-%m-%d %H:%M:%S.%f'):
                    transaction.price = Blockonomics.fetch_new_btc_price()

                # Convert satoshi to fiat
                satoshi = float(flask.request.args.get("value"))
                received_btc = satoshi/1.0e8
                received_value = received_btc*transaction.price
                print ("Recieved "+str(received_value)+" "+configloader.config["Payments"]["currency"]+" on address "+address)

                # Add the credit to the user account
                user = dbsession.query(db.User).filter(db.User.user_id == transaction.user_id).one_or_none()
                user.credit += received_value
                # Update the value + txid + status + timestamp for transaction in DB
                transaction.value += received_value
                transaction.txid = flask.request.args.get("txid")
                transaction.status = status
                transaction.timestamp = current_time
                print (transaction.value)
                # Add a transaction to list
                new_transaction = db.Transaction(user=user,
                                             value=received_value,
                                             provider="Bitcoin",
                                             notes = address)
                # Add and commit the transaction
                dbsession.add(new_transaction)
                dbsession.commit()
                return "Success"
            else:
                return "Transaction already proccessed"
        else:
            return "Not enough confirmations"
    else:
        return "Incorrect secret"

@app.route('/test_setup', methods=['GET', 'POST'])
def test_setup():
    response = Blockonomics.get_callbacks()
    error_str = ''
    print (response.json()[0]['address'])
    response_body = response.json()
    if response_body[0]:
        response_callback = response_body[0]['callback']
        response_address = response_body[0]['address']
    else :
        response_callback = ''
        response_address = ''
    print (response_address)
    callback_secret = configloader.config["Bitcoin"]["secret"]
    api_url = flask.url_for('callback', _external=True)
    callback_url = api_url + "?secret=" + callback_secret
    return_string = "Blockonomics Callback URL: " + callback_url
    # Remove http:# or https:# from urls
    api_url_without_schema = api_url.replace("https://","")
    api_url_without_schema = api_url_without_schema.replace("http://","")
    callback_url_without_schema = callback_url.replace("https://","")
    callback_url_without_schema = callback_url_without_schema.replace("http://","")
    response_callback_without_schema = response_callback.replace("https://","")
    response_callback_without_schema = response_callback_without_schema.replace("http://","")
    # TODO: Check This: WE should actually check code for timeout
    if response == False:
        error_str = 'Your server is blocking outgoing HTTPS calls'
    elif response.status_code==401:
        error_str = 'API Key is incorrect'
    elif response.status_code!=200:  
        error_str = response.text
    elif response_body == None or len(response_body) == 0:
        error_str = 'You have not entered an xpub'
    elif len(response_body) == 1:
        print ("response callback" + response_callback)
        if response_callback == "":
            print ("No callback URL set, set one")
            # No callback URL set, set one 
            Blockonomics.update_callback(callback_url, response_address)
        elif response_callback_without_schema != callback_url_without_schema:
            print ("callback URL set, checking secret")
            base_url = api_url_without_schema
            # Check if only secret differs
            if base_url in response_callback:
                # Looks like the user regenrated callback by mistake
                # Just force Update_callback on server
                Blockonomics.update_callback(callback_url, response_address)
            else:
                error_str = "You have an existing callback URL. Refer instructions on integrating multiple websites"
    else:
        error_str = "You have an existing callback URL. Refer instructions on integrating multiple websites"
        # Check if callback url is set
        for res_obj in response_body:
            res_url = res_obj['callback'].replace("https://","")
            res_url = res_url.replace("https://","")
            if res_url == callback_url_without_schema:
                error_str = ""
    if error_str == "":
        # Everything OK ! Test address generation
        response = Blockonomics.new_address(True)
        if response.status_code != 200:
            error_str = response.text
    if error_str:
        error_str = error_str + '<p>For more information, please consult <a href="https://blockonomics.freshdesk.com/support/solutions/articles/33000215104-troubleshooting-unable-to-generate-new-address" target="_blank">this troubleshooting article</a></p>'
        return error_str + '<br>' + return_string
    # No errors
    return 'Congrats ! Setup is all done<br>' + return_string

def flaskThread():
    app.run(threaded=True)

# Run the main function only in the main process
if __name__ == "__main__":
    # Start callback in thread
    threading.Thread(target=flaskThread).start()
    main()