!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

cisco_1921 = {
    'device_type': 'cisco_ios',
    'host': raw_input("What is the router's IP? "),
    'username': raw_input("What is your username? "),
    'password': getpass(),
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}
#Looks for a file called config
with open('config') as f:
    lines = f.read().splitlines()
#print lines #Optional, prints each line to be pushed to router
net_connect = ConnectHandler(**cisco_1921)
output = net_connect.send_config_set(lines)
print output 

net_connect.disconnect()
print ("Status: Successful!")
