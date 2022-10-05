import json
import requests
import time 
from bs4 import BeautifulSoup
from prettytable import PrettyTable


class breach:
    url = "https://leakcheck.net/api/public?key=49535f49545f5245414c4c595f4150495f4b4559&check={}"
    saven = "./vapi/save/nick.txt"
    savee = "./vapi/save/email.txt"

def run(email,nick):

    res_em = ""
    email_search = requests.get(breach.url.format(email)).text
    data_em = json.loads(email_search)
    n = len(data_em['sources'])
    data = data_em['sources']
    emc = PrettyTable()
    emc.field_names = ["Breach Name","Date"]
    for i in range(0,n):
        emc.add_row([data_em['sources'][i]["name"], data_em['sources'][i]["date"]])
    print(emc)

run("error","error")