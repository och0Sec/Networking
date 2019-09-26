#!/usr/bin/env python3
# Import Libraries
from netmiko import ConnectHandler
from getpass import getpass
import datetime
# Get the date
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
# Define username and password for cisco device
username = "user"
password = "passwd"
# Prompt for the Cisco Router's IP
remoteHost = input("What is the router's IP? ")
# Define Cisco Object
cisco_1921 = {
    'device_type': 'cisco_ios',
    'host': remoteHost,
    'username': username,
    'password': password,
    'port' : 22,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

# Connect to Cisco Router
print ("Connecting")
net_connect = ConnectHandler(**cisco_1921)
print ("Connected!\n")
hostname = net_connect.send_command('show run | i hostname')
hostname.split(" ")
col1,col2 = hostname.split(" ")
print("Working on " + col2)
filename = date + " " + col2 + ' startup-config'
showstart = net_connect.send_command('show start')
file = open(filename, "x")
file.write(showstart)
file.close()
