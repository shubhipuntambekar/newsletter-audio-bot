import os

import pywhatkit
import time
from dotenv import load_dotenv


load_dotenv()


def send_whatsapp_message(link):
    number = os.getenv("phone_number")
    msg = f"🎧 Your System Design audio is ready: {link}"
    pywhatkit.sendwhatmsg_instantly(number, msg, wait_time=4, tab_close=True)
    time.sleep(15)
