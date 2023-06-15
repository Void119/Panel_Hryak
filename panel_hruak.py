import requests
import time
  
from threading import Thread
from database import *

def auto_feed():
    if DataBase.learn("config.json")["feed"]:
        while True:
            response = requests.post('https://discord.com/api/v9/interactions', 
                                    headers={
                                        'Authorization': DataBase.learn("config.json")["token"], 
                                        'Content-Type': 'application/json'
                                    }, 
                                    json={ 'type': 2,
                                        'application_id': '1102273144733049003',
                                        'guild_id': DataBase.learn("config.json")["guild_id"], 
                                        'channel_id': DataBase.learn("config.json")["channel_id"], 
                                        "session_id":"3da3d64d2e4ed2e541a6394ecbfaaaa8",
                                        'data': {"version":"1107375400734179429","id":"1107375400734179428","name":"feed","type":1,"options":[],"application_command":{"id":"1107375400734179428","application_id":"1102273144733049003","version":"1107375400734179429","name":"feed","description":"-","description_localized":"Накормить своего хряка"},"attachments":[]},
                                        'nonce': str(int(time.time()))
                                    })

            print(f"Авто feed: {response.status_code}")
            time.sleep(DataBase.learn("config.json")["time_feed"])

def auto_meat():
    if DataBase.learn("config.json")["meat"]:
        while True:
            response = requests.post('https://discord.com/api/v9/interactions', 
                                    headers={
                                        'Authorization': DataBase.learn("config.json")["token"],  
                                        'Content-Type': 'application/json'
                                    }, 
                                    json={ 'type': 2,
                                        'application_id': '1102273144733049003',
                                        'guild_id': DataBase.learn("config.json")["guild_id"], #  
                                        'channel_id': DataBase.learn("config.json")["channel_id"], 
                                        "session_id":"3da3d64d2e4ed2e541a6394ecbfaaaa8",
                                        'data': {"version":"1108173842733613067","id":"1108173842733613066","name":"meat","type":1,"options":[],"application_command":{"id":"1108173842733613066","application_id":"1102273144733049003","version":"1108173842733613067","name":"meat","description":"-","description_localized":"Снять немного сала с вашего хряка (ему не больно)"},"attachments":[]},
                                        'nonce': str(int(time.time()))
                                    })

            print(f"Авто meat: {response.status_code}")
            time.sleep(DataBase.learn("config.json")["time_meat"])

Thread(target=auto_feed).start()
Thread(target=auto_meat).start()
