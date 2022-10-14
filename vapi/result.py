from vapi.poor import color
from rich.console import Console
from rich.tree import Tree

def print(nn,n,em,ph,loc,web,bio,bio2,loc2):
  console = Console()
  T = Tree("📂 Vector", guide_style="bold bright_black")
  
  if(nn!=None or n!=None):
    person = T.add("📃 Personal")
    if(nn!=None):
      person.add(f"📄 Nick Name : {nn}")
    if(n!=None):
      person.add(f"📄 Real Name : {n}")

  if(em!=None or ph!=None):
    contact = T.add("📮 Contact")
    if(em!=None):
      contact.add(f"📫 Email : {em}")
    if(ph!=None):
      contact.add(f"📫 Phone : {ph}")

  if(loc!=None):
    location = T.add("🏡 Location")
    location.add(f"🏡 Location : {loc}")
    for i in loc2:
      location.add(f"🏠 Possible : {i}")
      
  console.print(T)
