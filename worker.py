import multiprocessing
import telegram

class ChatWorker:
    """A worker for a single conversation. A new one should be created every time the /start command is sent."""

    def __init__(self, bot: telegram.Bot, chat: telegram.Chat):
        # A pipe connecting the main process to the chat process is created
        in_pipe, out_pipe = multiprocessing.Pipe(duplex=False)
        # The sending pipe is stored in the ChatWorker class, allowing the forwarding of messages to the chat process
        self.pipe = in_pipe
        # A new process running the conversation handler is created, and the receiving pipe is passed to its arguments to enable the receiving of messages
        self.process = multiprocessing.Process(target=conversation_handler, args=(bot, chat, out_pipe))

    def start(self):
        """Start the worker process."""
        self.process.start()

    def stop(self):
        # Gracefully stop the worker process
        # TODO: send a stop message to the process
        raise NotImplementedError()
        # Wait for the process to stop
        self.process.join()


def conversation_handler(bot: telegram.Bot, chat: telegram.Chat, pipe: multiprocessing.Connection):
    raise NotImplementedError()