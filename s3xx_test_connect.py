#!/usr/bin/env python3
'''
YOUR CISCO SG300 OR SG350 SWITCH MUST ALREADY HAVE THIS IN ITS CONFIGURATION:
CONFIGURE TERMINAL
IP SSH PASSWORD-AUTH
END
WR
Y
'''

from netmiko import ConnectHandler
from getpass import getpass

cisco_s300 = {
    'device_type': 'cisco_s300',
    'host': 'SG300_Switch_IP',
    'username': input("What is your username? "),
    'password': getpass(),
    'global_delay_factor': 2,
}

net_connect = ConnectHandler(**cisco_s300)
print('---cONNECTED---')
print(net_connect.find_prompt())
net_connect.disconnect()
