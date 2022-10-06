import requests
from vapi.poor import color
from pyvis.network import Network
from vapi.breach import breach_nickname
import eel

def vis(nickname,name,locations,email,social):
    print(f"{color.CBLUE}[*]{color.CWHITE2} Vector{color.CWHITE} -->{color.CWHITE2} Netvapi{color.CWHITE} loading collected osint informations and creating graph...")
    
    net = Network(height="750px", width="100%", bgcolor="#29292E", font_color="#FFFFFF") # directed =True
    net.add_node(0,nickname,color="#E74C3C")
    net.toggle_physics(True)
    
    net.add_node("social","Social Media",color="#6C3483")
    net.add_edge(0,"social",size=2)

    if(len(locations)!=0):
        net.add_node("locations","Locations",color="#6C3483")
        net.add_edge(0,"locations",size=2)
        for o in range(0,len(locations)):
            net.add_node(f"locations{o}",locations[o],color="#2C3E50")
            net.add_edge("locations",f"locations{o}")

    bleaks = False
    if(breach_nickname(nickname)!="false"):
        bleaks = True
        leaks = breach_nickname(nickname)
        net.add_node("leaks","Leaks",color="#6C3483")
        net.add_edge(0,"leaks",size=2)
        m = len(leaks)
        for p in range(0,m):
            net.add_node(f"leaks{p}",leaks[p],color="#28B463")
            net.add_edge("leaks",f"leaks{p}")

    for i in range(0,len(social)):
        net.add_node(f"social{i}",social[i],color="#2E86C1")
        net.add_edge("social",f"social{i}")

    net.repulsion(node_distance=200, spring_length=300)
    #net.show_buttons(filter_=True)
    net.save_graph(f"{nickname}.html")
    #eel.start("./vis/nodes.html")

#vis("error","saderror","bla bla","bla bla","bla bla","bla bla","bla bla")