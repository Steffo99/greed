import threading
import telegram
import strings
import configloader
import sys
import queue as queuem

# Load the configuration
config = configloader.load_config()

class StopSignal:
    """A data class that should be sent to the worker when the conversation has to be stopped abnormally."""

    def __init__(self, reason: str=""):
        self.reason = reason


class ChatWorker:
    """A worker for a single conversation. A new one should be created every time the /start command is sent."""

    def __init__(self, bot: telegram.Bot, chat: telegram.Chat):
        # The sending pipe is stored in the ChatWorker class, allowing the forwarding of messages to the chat process
        self.queue = queuem.Queue()
        # A new thread running the conversation handler is created, and the queue is passed to its arguments to enable the receiving of messages
        self.thread = threading.Thread(target=conversation_handler, args=(bot, chat, self.queue))

    def start(self):
        """Start the worker process."""
        self.thread.start()

    def stop(self, reason: str=""):
        """Gracefully stop the worker process"""
        # Send a stop message to the thread
        self.queue.put(StopSignal(reason))
        # Wait for the thread to stop
        self.thread.join()

# TODO: maybe move these functions to a class

def graceful_stop(bot: telegram.Bot, chat: telegram.Chat, queue):
    """Handle the graceful stop of the process."""
    # Notify the user that the session has expired
    bot.send_message(chat.id, strings.conversation_expired)
    # End the process
    sys.exit(0)

def receive_next_update(bot: telegram.Bot, chat: telegram.Chat, queue) -> telegram.Update:
    """Get the next update from a pipe.
    If no update is found, block the process until one is received.
    If a stop signal is sent, try to gracefully stop the process."""
    # Pop data from the queue
    try:
        data = queue.get(timeout=int(config["Telegram"]["conversation_timeout"]))
    except queuem.Empty:
        # If the conversation times out, gracefully stop the thread
        graceful_stop(bot, chat, queue)
    # Check if the data is a stop signal instance
    if isinstance(data, StopSignal):
        # Gracefully stop the process
        graceful_stop(bot, chat, queue)
    # Return the received update
    return data


def conversation_handler(bot: telegram.Bot, chat: telegram.Chat, queue):
    """This function is ran once for every conversation (/start command) by a separate process."""
    # TODO: catch all the possible exceptions
    # Welcome the user to the bot
    bot.send_message(chat.id, strings.conversation_after_start)
    # TODO: Send a command list or something
    while True:
        # For now, echo the sent message
        update = receive_next_update(bot, chat, queue)
        bot.send_message(chat.id, f"{threading.current_thread().name} {update.message.text}")