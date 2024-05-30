import time
import random
import requests
from faker import Faker
from colorama import Fore, Style, init

# Initialize colorama
init()
fake = Faker()

# Replace with your own token and chat IDs
TOKEN = '6681604946:AAF9aIYvwh5qvyaM-OErSeh2Bk9vKCNMWs8'
CHAT_IDS = [ '-4233485302']   # Replace with your target chat IDs

# URL to send messages
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

def get_random_password():
    # Generate a random password or read from a file
    # For simplicity, we'll generate a random password here
    return fake.password()

def get_random_ip():
    return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

def get_country_info(ip):
    # Use a free IP geolocation API
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            return data['country'], data['countryCode'], data['regionName']
        else:
            return 'Unknown', 'XX', 'Unknown'
    except Exception as e:
        return 'Unknown', 'XX', 'Unknown'

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
            identity = fake.user_name()
            password = get_random_password()
            ip = get_random_ip()
            country, country_code, state = get_country_info(ip)
            
            message = (
                f"Result from IpAddress for user {identity} is:\n"
                f" - Username/Email: {identity}\n"
                f" - Password: @SupraFreak\n"
                f" - IPAddress: {ip}\n"
                f" - Country: {country}\n"
                f" - Country-code: {country_code}\n"
                f" - State: {state}"
            )
            
            send_message_to_chat(chat_id, message)
        time.sleep(15)
