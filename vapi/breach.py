import json
import requests
import time 
from bs4 import BeautifulSoup
from prettytable import PrettyTable

from vapi.poor import color
from vapi.error import exp

class breach:
    url = "https://leakcheck.net/api/public?key=49535f49545f5245414c4c595f4150495f4b4559&check={}"
    saven = "./vapi/save/nick.txt"
    savee = "./vapi/save/email.txt"

def breach_nickname(nickname):
    nick_search = requests.get(breach.url.format(nickname)).text
    data_nc = json.loads(nick_search)
    leaks = []
    if(data_nc['success']==True):
        c = len(data_nc['sources'])
        res = f"""{color.CBLUE}[*]{color.CWHITE} Found {color.CWHITE2}{data_nc['found']}{color.CWHITE} data leaks include {color.CWHITE2}{nickname}{color.CWHITE} with {color.CWHITE2}{data_nc['passwords']}{color.CWHITE} passwords!"""
        print(res)
        for j in range(0,c):
            leaks.append(data_nc['sources'][j]["name"])
    else:
        return "false"

    return leaks


def run(email,nick):
    time.sleep(2)
    print(f"""
{color.CGREEN}[//]{color.CWHITE} This action will search the following informations below in {color.CWHITE2}breached databases{color.CWHITE}...
{color.CGREEN}[{time.strftime("%X")}] {color.CWHITE}Email Adress : {color.CWHITE}[{color.CWHITE2}{email}{color.CWHITE}]
{color.CGREEN}[{time.strftime("%X")}] {color.CWHITE}Username     : {color.CWHITE}[{color.CWHITE2}{nick}{color.CWHITE}]
    """)
    try:

        linfo = PrettyTable()
        linfo.field_names = ["Breach Name","Date","Include"]
        if(email!=None):
            email_search = requests.get(breach.url.format(email)).text
            data_em = json.loads(email_search)
            n = len(data_em['sources'])
            if(data_em['success']==True):
                res = f"""{color.CBLUE}[*]{color.CWHITE} Found {color.CWHITE2}{data_em['found']}{color.CWHITE} data leaks include {color.CWHITE2}{email}{color.CWHITE} with {color.CWHITE2}{data_em['passwords']}{color.CWHITE} passwords!"""
                print(res)
                for i in range(0,n):
                    linfo.add_row([data_em['sources'][i]["name"], data_em['sources'][i]["date"],email])
            else:
                nf = f"[{color.CRED}!{color.CWHITE}] Not found any {color.CWHITE2}leak{color.CWHITE} for [{color.CWHITE2}{email}{color.CWHITE}]!"
        
        if(nick!=None):
            nick_search = requests.get(breach.url.format(nick)).text
            data_nc = json.loads(nick_search)
            c = len(data_nc['sources'])
            if(data_nc['success']==True):
                res = f"""{color.CBLUE}[*]{color.CWHITE} Found {color.CWHITE2}{data_nc['found']}{color.CWHITE} data leaks include {color.CWHITE2}{nick}{color.CWHITE} with {color.CWHITE2}{data_nc['passwords']}{color.CWHITE} passwords!"""
                print(res)
                for j in range(0,c):
                    linfo.add_row([data_nc['sources'][j]["name"], data_nc['sources'][j]["date"],nick])
            else:
                nf = f"[{color.CRED}!{color.CWHITE}] Not found any {color.CWHITE2}leak{color.CWHITE} for [{color.CWHITE2}{nick}{color.CWHITE}]!"
        
        print(linfo)
        print(nf)
    except:
        pass