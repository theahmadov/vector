from vapi.poor import color
from vapi.visvapi import netvapi 

def run(name,location,email,web,bio,social):
    print("")
    netvapi.vis(name,location,email,web,bio,social)