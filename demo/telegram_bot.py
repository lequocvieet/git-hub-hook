import requests

import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_API=os.getenv('TELEGRAM_API')
BOT_TOKEN=os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID=os.getenv("CHAT_ID")


# def Get_Group_Chat_ID(GROUP_NAME):
#     res = requests.get(url=TELEGRAM_API+BOT_TOKEN+"/getUpdates")
#     print(res)
#     return 

def Send_Message(DATA):
    request = {
        "chat_id": CHAT_ID,
        "text": DATA,
        "parse_mode": "HTML"
    }
    res = requests.post(url=TELEGRAM_API+BOT_TOKEN+"/sendMessage", json=request)
    print("response chat",res)
    return res
