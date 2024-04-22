import os
import time
from dotenv import load_dotenv

import requests
import telebot
import logging

load_dotenv(verbose=True)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    logger.info(message)
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def get_cities(message):
    bot.send_message(message.chat.id, message.text)
    # logger.info(message)


if __name__ == '__main__':
    # bot.polling(none_stop=True, interval=0)
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(5)
