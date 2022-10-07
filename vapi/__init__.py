from vapi.poor import color
#from vapi import _social as social
from vapi import social
from vapi import breach
from vapi import geo
import time
import os 
import sys

def clear():
    os.system("cls || clear")

def help():
    print(f"""
{color.CBLUE}-V-{color.CWHITE}
Vector Help Guide : 

- Osint : Username Scan
{color.CVIOLET}${color.CWHITE} python vector.py username

- Osint : Email Scan
{color.CVIOLET}${color.CWHITE} python vector.py emailadress

- Osint : IP Info
{color.CVIOLET}${color.CWHITE} python vector.py xxx.xxx.xxx.xxx

{color.CBLUE}*{color.CWHITE} Vector is easy to use. You just need target in any type. Just use vector in this format : python vector.py target...
Vector will automaticly understand what is your target type. And will start scan for that information.
{color.CBLUE}*{color.CWHITE} After username scan {color.CBLUE}Vector{color.CWHITE} will show graph report.
    """)
"""
Thesaderror sample osint text:
thesaderror#1351
"""
def T():
    print(f"{color.CBOLD}{color.CBLUE}[*]{color.CWHITE} Starting {color.CWHITE2}Vector{color.CWHITE}...")
    time.sleep(1)
    print(f"{color.CBLUE}[/-/]{color.CBLUE} Thesaderror",end="\r")
    time.sleep(0.5)
    print(f"{color.CBLUE}[/-/]{color.CRED} Thesaderror",end="\r")
    time.sleep(0.5)
    print(f"{color.CBLUE}[/-/]{color.CGREEN} Thesaderror",end="\r")
    time.sleep(1)
    Tz = f"""\n{color.CWHITE2}Hey! Let me explain myself. I am Thesaderror and also owner of {color.CRED}Vector{color.CWHITE2} project...
I am from {color.CBLUE}Azerbaijan{color.CWHITE2}. I am competitive programmer and cyber security student. I
learn {color.CBLUE}python{color.CWHITE2} & {color.CVIOLET}C/C++{color.CWHITE2} and also using them in my projects.

I am in these platforms : 

{color.CBEIGE}Github  {color.CWHITE2}: https://github.com/thesaderror
{color.CBEIGE}Discord {color.CWHITE2}: thesaderror#1351 
{color.CBEIGE}BreachForums {color.CWHITE2}: https://breached.to/User-saderror
  
- Lol this is not me :
https://www.instagram.com/thesaderror/
    """
    print(Tz)

"""
Hawkings sample osint text:
Shahin#2317
"""
def H():
    print(f"{color.CBOLD}{color.CBLUE}[*]{color.CWHITE} Starting {color.CWHITE2}Vector{color.CWHITE}...")
    time.sleep(1)
    print(f"{color.CBLUE}[|-|]{color.CBLUE} H4wK1n6",end="\r")
    time.sleep(0.5)
    print(f"{color.CBLUE}[|-|]{color.CRED} H4wK1n6",end="\r")
    time.sleep(0.5)
    print(f"{color.CBLUE}[|-|]{color.CGREEN} H4wK1n6",end="\r")
    time.sleep(1)
    print(f"""Hey! You wanted to get some information about {color.CRED} H4wK1n6! Allright....""")
    time.sleep(0.4)
    print(f"""
I am an experienced {color.CRED}competitive/robotics{color.CWHITE} programmer and {color.CRED}cyber{color.CWHITE} security student. I am 
from {color.CBLUE}Aze{color.CRED}rbai{color.CGREEN}jan{color.CWHITE}. I know C/C++(Using since I was 6 years old). And learnt python(still evolving).
Here is my contact information :
{color.CBLUE}[*]{color.CWHITE} Discord : Shahin#2317
{color.CBLUE}[*]{color.CWHITE} Github  : https://github.com/shalekberli
    """)

def cli(nick):   
    print(f"{color.CBLUE}[*]{color.CWHITE} Starting {color.CWHITE2}Vector{color.CWHITE}...")
    time.sleep(1)
    print(f"{color.CBLUE}[*]{color.CWHITE2} Vector{color.CWHITE} social osint : ")
    social.run(nick)

def email(email,nick):
    print(f"{color.CBLUE}[*]{color.CWHITE} Starting {color.CWHITE2}Vector{color.CWHITE}...")
    time.sleep(1)
    print(f"{color.CBLUE}[*]{color.CWHITE2} Vector{color.CWHITE} leak checker : ")
    breach.run(email,nick)

def geos(ip):
    print(f"{color.CBLUE}[*]{color.CWHITE} Starting {color.CWHITE2}Vector{color.CWHITE}...")
    time.sleep(1)
    print(f"{color.CBLUE}[*]{color.CWHITE2} Vector{color.CWHITE} geo info sniper : ")
    geo.run(ip)

def web():
    print(f"{color.CRED}Vector W-GUI will be avaliable soon. Please be in pation...")
