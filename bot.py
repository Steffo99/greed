from telegram.ext import Updater
import logging
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    bot = Updater(os.environ("telegram_api_key"))
    bot.start_polling()
    bot.idle()