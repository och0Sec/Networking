from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco_s300 = {
    'device_type': 'cisco_s300',
    'host': '192.168.x.x',
    'username': 'cisco',
    'password': getpass()

}

net_connect = ConnectHandler(**cisco_s300)
print('---cONNECTED---')
#print(net_connect.find_prompt())
output = net_connect.send_command('show int stat')
lines = output.splitlines()[4:-12] #<-remove the heading and footer of a 10 port gig switch.
print('Line Count: ' + str(len(lines))) #<- prints count lines.
for line in lines: #<-splits each line into words.
    words = line.split()
    print(len(words),words)
net_connect.disconnect()
