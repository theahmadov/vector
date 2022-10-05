import requests
import json
from vapi.poor import color

def run(ip):
    req = requests.get(f"http://ip-api.com/json/{ip}").text
    data = json.loads(req)
    print(f'''
{color.CBLUE}[*]{color.CWHITE} IP Information :
{color.CWHITE}IP Adress  : [{color.CWHITE2}{ip}{color.CWHITE}]
{color.CWHITE}Status     : [{color.CWHITE2}{data["status"]}{color.CWHITE}]
{color.CWHITE}Country    : [{color.CWHITE2}{data["country"]}{color.CWHITE}]
{color.CWHITE}TimeZone   : [{color.CWHITE2}{data["timezone"]}{color.CWHITE}]
{color.CWHITE}City       : [{color.CWHITE2}{data["city"]}{color.CWHITE}]
{color.CWHITE}ORG Name   : [{color.CWHITE2}{data["org"]}{color.CWHITE}]
{color.CWHITE}ZIP        : [{color.CWHITE2}{data["zip"]}{color.CWHITE}]
{color.CWHITE}[{color.CWHITE2}Potantial{color.CWHITE}] Map  : [{color.CWHITE2}https://www.google.com/maps/search/{data["lat"]}+{data["lon"]}{color.CWHITE}]
    ''')