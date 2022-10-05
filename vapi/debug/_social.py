import json
import requests
import time
from bs4 import BeautifulSoup

from vapi.poor import color
from vapi.error import exp
from vapi.bios import biose
from vapi import breach

class info:
    nickname = None
    name = None
    location = None
    email = ""
    bio = None
    web = None

class social:
    save = "./vapi/save/info.txt"
    social_json = "./vapi/vapi_db/social.json"

    with open(social_json, "r") as f:
        data = json.loads(f.read())


def scrape_c(classname, website):
    try:
        if classname.startswith("span::"):
            classname = classname.split("span::")[1]
            req = requests.get(website).text
            soup = BeautifulSoup(req, "html.parser")
            # cll = soup.find(class_=classname)
            cll = soup.find("span", {"class": classname})
            if cll.text != None:
                return cll.text
            else:
                return "nothing"

        elif classname.startswith("div::"):
            classname = classname.split("div::")[1]
            req = requests.get(website).text
            soup = BeautifulSoup(req, "html.parser")
            # cll = soup.find(class_=classname)
            cll = soup.find("div", {"class": classname})
            if cll.text != None:
                cll = cll.text.split()
                out = ""
                for i in cll:
                    out += i + " "
                return out
            else:
                return "nothing"

        elif classname.startswith("p::"):
            classname = classname.split("p::")[1]
            req = requests.get(website).text
            soup = BeautifulSoup(req, "html.parser")
            # cll = soup.find(class_=classname)
            cll = soup.find("p", {"class": classname})
            if cll.text != None:
                return cll.text
            else:
                return "nothing"
        elif classname.startswith("ul::"):
            classname = classname.split("ul::")[1]
            req = requests.get(website).text
            soup = BeautifulSoup(req, "html.parser")
            # cll = soup.find(class_=classname)
            cll = soup.find("ul", {"class", classname})
            if cll.text != None:
                return cll.text
            else:
                return "nothing"
    except:
        return "nothing"


def itype(clt, dt):
    if dt != None and type(dt)!=int:
        if type(dt) != int and type(dt) != float:
            itype("Location", biose(dt, "loc"))
            itype("Email", biose(dt, "mail"))
            itype("Website", biose(dt, "site"))

        if clt == "Bio":
            if info.bio == None:
                info.bio = dt
            else:
                if len(info.bio) < len(dt):
                    info.bio = dt

        elif clt == "Real Name":
            if info.name == None:
                info.name = dt
            else:
                if len(info.name) < len(dt):
                    info.name = dt

        elif clt == "Website":
            if info.web == None:
                info.web = dt
            else:
                if len(info.web) < len(dt):
                    info.web = dt

        elif clt == "Location":
            if info.location == None:
                info.location = dt
            else:
                if len(str(info.location)) < len(dt):
                    info.location = dt

        elif clt == "Email":
            if info.email == None:
                info.email = dt
            else:
                if len(info.email) < len(dt):
                    info.email = dt

def exp_check(n):
    try:
        requests.get("https://1.1.1.1/")
    except:
        code = "0x1"
    try:
        url = social.data[f"{n}"]["look"].split("{}/")[0]
        requests.get(url)
        print(url)
    except:
        code = "0x2"
        parm = url
    lst = [code,parm]
    return lst

def run(nick):
    info.nickname = nick
    # print(f"Hello {nick}!")

    for n in range(1, social.data["count"] + 1):
        minfo = f' {color.CWHITE}# Type : {social.data[f"{n}"]["type"]} * Country : {social.data[f"{n}"]["cn"]}'
        look = social.data[f"{n}"]["look"].format(nick)
        problem = False
        try:
            req = requests.get(look)
        except:
            problem = True


        if problem == False:
            if type(social.data[f"{n}"]["nf"]) == int:
                if(req.status_code != social.data[f"{n}"]["nf"]):
                    if (social.data[f"{n}"]["cll"] != "None" and scrape_c(social.data[f"{n}"]["cll"], look) != "nothing"):
                        print(f'{color.CGREEN}[{time.strftime("%X")}] {color.CWHITE2}{social.data[f"{n}"]["name"]} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)} {minfo}')
                        scc = scrape_c(social.data[f"{n}"]["cll"], look)
                        itype(social.data[f"{n}"]["cll_t"], scc)
                        print(f"""{color.CBLUE}[+] {color.CWHITE}{social.data[f"{n}"]["cll_t"]} : {color.CWHITE2}{scc}""")
                    else:
                        print(f'{color.CGREEN}[{time.strftime("%X")}] {color.CWHITE2}{social.data[f"{n}"]["name"]} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)} {minfo}')
            else:
                if((social.data[f"{n}"]["nf"] in req.text) == False):
                    if (social.data[f"{n}"]["cll"] != "None" and scrape_c(social.data[f"{n}"]["cll"], look) != "nothing"):
                        print(f'{color.CGREEN}[{time.strftime("%X")}] {color.CWHITE2}{social.data[f"{n}"]["name"]} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)} {minfo}')
                        scc = scrape_c(social.data[f"{n}"]["cll"], look)
                        itype(social.data[f"{n}"]["cll_t"], scc)
                        print(f"""{color.CBLUE}[+] {color.CWHITE}{social.data[f"{n}"]["cll_t"]} : {color.CWHITE2}{scc}""")
                    else:
                        print(f'{color.CGREEN}[{time.strftime("%X")}] {color.CWHITE2}{social.data[f"{n}"]["name"]} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)} {minfo}')

        else:
            expc = exp_check(n)
            print(exp(expc[0],expc[1],nick))
            problem = False

    print(
        f"""
{color.CBLUE}[*]{color.CWHITE2} Vector Social Osint Result :
    Nick Name : {info.nickname}
    Real Name : {info.name}
    Location  : {info.location}
    Email     : {info.email}
    Bio       : {info.bio}
    Web       : {info.web}
    """)

    time.sleep(1)
    breach.run(None,nick)