#Author: Oto Ricardo
#Date: 7/31/19
#pingFromRemoteHost.py 
#SSH into a remote cisco router and ping a know hard-codede IP, returns the output from remote cisco router.

from netmiko import ConnectHandler
import getpass

host = raw_input("What is the router's IP? ")
username = "DOMAIN\\" + raw_input("What is your username? ")
password = getpass.getpass()
cisco_1921 = {
    'device_type': 'cisco_ios',
    'host':   host,
    'username': username,
    'password': password,
    'port' : 22,          # optional, defaults to 22
    'secret': '##F1rst##F1rst',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_1921)

output = net_connect.send_command('ping 10.10.254.1 re 10')
print(output)


