import json
import requests
import time
from bs4 import BeautifulSoup

from vapi.poor import color
from vapi.error import exp
from vapi.bios import biose
from vapi import breach
from vapi import visvapi
from vapi import result

class info:
    nickname = None
    name = None
    location = None
    locations = []
    email = ""
    bio = None
    web = None
    bio_s = []
    phone = None


class social:
    save = "./vapi/save/info.txt"
    social_json = "./vapi/vapi_db/social.json"
    config_json = "config.json"
    style = ""
    with open(config_json,"r") as c:
        data = json.loads(c.read())
        style = data["style"]
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

        elif classname.startswith("text"):
            cll = requests.get(website).text
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
        elif classname.startswith("body"):
            req = requests.get(website).text
            soup = BeautifulSoup(req, "html.parser")
            # cll = soup.find(class_=classname)
            cll = soup.body
            if cll.text != None:
                return cll.text
            else:
                return "nothing"

        elif classname.startswith("json::"):
            classname = classname.split("json::")[1]
            req = requests.get(website).text
            data = json.loads(req)
            cll = data[classname]
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
            info.bio_s.append(dt)
            if(biose(dt, "phone_num")!="invalid"):
                info.phone = biose(dt, "phone_num")
                
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
            info.locations.append(dt)
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
    social_links = []
    info.nickname = nick
    # print(f"Hello {nick}!")

    for n in range(1, social.data["count"] + 1):
        look = social.data[f"{n}"]["look"].format(nick)
        problem = False
        try:
            req = requests.get(look)
        except:
            problem = True

        if(social.style=="E0"):
            if problem == False:
                if type(social.data[f"{n}"]["nf"]) == int:
                    if(req.status_code != social.data[f"{n}"]["nf"]):
                        if (social.data[f"{n}"]["cll"] != "None" and scrape_c(social.data[f"{n}"]["cll"], look) != "nothing"):
                            scc = scrape_c(social.data[f"{n}"]["cll"], look)
                            itype(social.data[f"{n}"]["cll_t"], scc)
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f"""[{color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE}]{color.CGREEN}[{color.CWHITE}
                            
        {nick} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}
        {color.CWHITE}Type : {color.CWHITE2}{social.data[f"{n}"]["type"]}
        {color.CWHITE}Most used Country :{color.CWHITE2} {social.data[f"{n}"]["cn"]}
        {color.CBLUE}[+] {color.CWHITE}{social.data[f"{n}"]["cll_t"]} : {color.CWHITE2}{scc}                   
{color.CGREEN}]{color.CWHITE}""")
                            
                            
                        else:
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f"""[{color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE}]{color.CGREEN}[{color.CWHITE}

        {nick} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}
        {color.CWHITE}Type : {color.CWHITE2}{social.data[f"{n}"]["type"]}
        {color.CWHITE}Most used Country :{color.CWHITE2} {social.data[f"{n}"]["cn"]}              
{color.CGREEN}]{color.CWHITE}""")
                else:
                    if((social.data[f"{n}"]["nf"] in req.text) == False):
                        if (social.data[f"{n}"]["cll"] != "None" and scrape_c(social.data[f"{n}"]["cll"], look) != "nothing"):
                            scc = scrape_c(social.data[f"{n}"]["cll"], look)
                            itype(social.data[f"{n}"]["cll_t"], scc)
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f"""[{color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE}]{color.CGREEN}[{color.CWHITE}

        {nick} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}
        {color.CWHITE}Type : {color.CWHITE2}{social.data[f"{n}"]["type"]}
        {color.CWHITE}Most used Country :{color.CWHITE2} {social.data[f"{n}"]["cn"]}
        {color.CBLUE}[+] {color.CWHITE}{social.data[f"{n}"]["cll_t"]} : {color.CWHITE2}{scc}                   
{color.CGREEN}]{color.CWHITE}""")
                            
                        else:
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f"""[{color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE}]{color.CGREEN}[{color.CWHITE}

        {nick} {color.CBLUE}--> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}
        {color.CWHITE}Type : {color.CWHITE2}{social.data[f"{n}"]["type"]}
        {color.CWHITE}Most used Country :{color.CWHITE2} {social.data[f"{n}"]["cn"]}                  
{color.CGREEN}]{color.CWHITE}""")

            else:
                expc = exp_check(n)
                print(exp(expc[0],expc[1],nick))
                problem = False
                
        elif(social.style=="E1"):
            if problem == False:
                if type(social.data[f"{n}"]["nf"]) == int:
                    if(req.status_code != social.data[f"{n}"]["nf"]):
                        if (social.data[f"{n}"]["cll"] != "None" and scrape_c(social.data[f"{n}"]["cll"], look) != "nothing"):
                            scc = scrape_c(social.data[f"{n}"]["cll"], look)
                            itype(social.data[f"{n}"]["cll_t"], scc)
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f'''{color.CGREEN}[{time.strftime("%R")}] {color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE} --> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}
{color.CBLUE}[!] {color.CWHITE2}{social.data[f"{n}"]["cll_t"]} : {scc}''')
                            
                            
                        else:
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f'''{color.CGREEN}[{time.strftime("%R")}] {color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE} --> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}''')
                else:
                    if((social.data[f"{n}"]["nf"] in req.text) == False):
                        if (social.data[f"{n}"]["cll"] != "None" and scrape_c(social.data[f"{n}"]["cll"], look) != "nothing"):
                            scc = scrape_c(social.data[f"{n}"]["cll"], look)
                            itype(social.data[f"{n}"]["cll_t"], scc)
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f'''{color.CGREEN}[{time.strftime("%R")}] {color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE} --> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}
{color.CBLUE}[!] {color.CWHITE2}{social.data[f"{n}"]["cll_t"]} : {scc}''')
                            
                        else:
                            social_links.append(social.data[f"{n}"]["name"])
                            print(f'''{color.CGREEN}[{time.strftime("%R")}] {color.CWHITE2}{social.data[f"{n}"]["name"]}{color.CWHITE} --> {color.CWHITE2}{social.data[f"{n}"]["look"].format(nick)}''')

            else:
                expc = exp_check(n)
                print(exp(expc[0],expc[1],nick))
                problem = False

    print(f"""
{color.CBLUE}[*]{color.CWHITE2} Vector Social Osint Result :
    Nick Name : {info.nickname}
    Real Name : {info.name}
    Location  : {info.location}
    Email     : {info.email}
    Bio       : {info.bio}
    Web       : {info.web}
    Phone Num : {info.phone}
    """)
    
    
    nickname = info.nickname
    name = info.name 
    locations= info.locations
    email = info.email
    bio_s = info.bio_s
    breach.run(None,nick)
    visvapi.run(nickname,name,locations,email,social_links)
