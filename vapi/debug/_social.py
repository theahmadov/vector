import json
import requests
import time
from bs4 import BeautifulSoup

class social:
    save = "./vapi/save/info.txt"
    social_json = "./vapi/vapi_db/social.json"

    with open(social_json, "r") as f:
        data = json.loads(f.read())

def run(nick):

    for n in range(1, social.data["count"] + 1):
        look = social.data[f"{n}"]["look"].format(nick)
        print(f'[{social.data[f"{n}"]}]({look})')
