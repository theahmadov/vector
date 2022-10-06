from vapi.poor import color
from vapi.visvapi import netvapi 

def run(nickname,name,locations,email,social_links):
    netvapi.vis(nickname,name,locations,email,social_links)