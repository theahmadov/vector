import requests
#from vapi.poor import color
from pyvis.network import Network

def vis(name,location,email,web,bio,social):
    net = Network()
    net.add_node(1,label=name)
    net.add_node(2,label=location)
    net.show("nodes.html")
    #print(name)

#vis("error","saderror","bla bla","bla bla","bla bla","bla bla")