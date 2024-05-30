import time
import random
import requests
from colorama import Fore, Style, init

# Initialize colorama
init()

# Replace with your own token and chat IDs
# Configuration
TOKEN = '6681604946:AAF9aIYvwh5qvyaM-OErSeh2Bk9vKCNMWs8'
CHAT_IDS = ['539647904', '-4233485302']  # replace with actual chat IDs
MESSAGES = [
    '',''
    
    # Add as many messages as you want
]

# Telegram API URL
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

def send_message_to_chat(chat_id, message):
    url = f'{BASE_URL}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print(Fore.GREEN + f"Message sent to chat ID {chat_id}: {message}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Failed to send message to chat ID {chat_id}: {response.json()}" + Style.RESET_ALL)

if __name__ == '__main__':
    print(Fore.CYAN + r"""
  _______ _______ ______ _______ _______  _____  _______
 |  _____ |______ |_____/ |______ |       |_____]    |
 |_____|  |______ |    \_ |______ |_____  |       __|__

 Developed by: @Vishwajithshaijukumar
 """ + Style.RESET_ALL)

    while True:
        for chat_id in CHAT_IDS:
            random_message = random.choice(MESSAGES)
            send_message_to_chat(chat_id, random_message)
        time.sleep(15)
 
