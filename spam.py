import logging
from telegram import Bot
from telegram.error import TelegramError
from termcolor import colored
import time
from art import *
import random  # Import random library

# Configuration
API_TOKEN = ''
CHAT_IDS = ['5357895784', '6505857897']  # replace with actual chat IDs
MESSAGES = [
    '',
    '',
    '',
    # Add as many messages as you want
]
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)

# Display colorful ASCII art logo
ascii_logo = text2art("TGscamSPAM")
print(colored(ascii_logo, 'green'))
print(colored('Developed by: @Vishwajithshaijukumar', 'yellow'))

def send_random_message(chat_id):
    message = random.choice(MESSAGES)
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print(colored(f'Message sent to {chat_id}: "{message}"', 'green'))
    except TelegramError as e:
        print(colored(f'Failed to send message to {chat_id}: {str(e)}', 'red'))

if __name__ == '__main__':
    while True:
        for chat_id in CHAT_IDS:
            send_random_message(chat_id)
        time.sleep(15)
