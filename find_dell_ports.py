from netmiko import ConnectHandler
from Crypto.Cipher import AES
from pprint import pprint
import getpass
import base64

dell = ['f8db88', 'f8cab8', 'f8bc12', 'f8b156', 'f48e38', 'f04da2', 'f01faf', 'ecf4bb', 'e4f004', 'e0db55', 'e0d848', 'd89ef3', 'd4bed9', 'd4ae52', 'd481d7', 'd09466', 'd067e5', 'd0431e', 'c81f66', 'bc305b', 'b8ca3a', 'b8ac6f', 'b82a72', 'b4e10f', 'b083fe', 'a4badb', 'a44cc8', 'a41f72', '989096', '9840bb', '90b11c', '8cec4b', '8ccf09', '848f69', '847beb', '842bbc', '842b2b', '801844', '7cc95a', '7845c4', '782bcb', '74e6e2', '74867a', '64006a', '5cf9dd', '5c260a', '588a5a', '549f35', '509a4c', '4c7625', '484d7e', '44a842', '405cfd', '34e6d7', '3417eb', '28f10e', '28c825', '24b6fd', '246e96', '204747', '20040f', '1c4024', '18fb7b', '18dbf2', '18a99b', '1866da', '180373', '14feb5', '14b31f', '149ecf', '141877', '109836', '107d1a', '08001b', '00c04f', '00b0d0', '006048', '0026b9', '0025bd', '002564', '0024e8', '0023ae', '002219', '00219b', '002170', '001ec9', '001e4f', '001d09', '001c23', '001bc5023', '001aa0', '0019b9', '00188b', '0016f0', '0015c5', '001530', '001422', '001372', '001248', '00123f', '001143', '000f1f', '000d56', '000bdb', '000874', '00065b', '000144', '000097']

ip_addr = input('Enter Switch IP: ')
USER = input('Enter username: ')
PASSWORD = getpass('Enter password: ')
User_Vlan = input('Enter user VLAN: ')

cisco_sw = {
	'device_type': 'cisco_s300',
	'host': ip_addr,
	'username': USER,
	'password': PASSWORD,
}

config = []
trunks = []

#### THIS SECTION USES CDP NEIGHBORS TO IDENTIFY THE TRUNK PORTS ###
net_connect = ConnectHandler(**cisco_sw)
output = net_connect.send_command('show cdp neigh')
lines = output.splitlines()[9:]

for line in lines:
	words = line.split()
	if len(words) > 5:
	    if 'Cisco' in words or 'cisco' in words:
            trunks.append(words[1])

### show mac address table and identifies Dell PCs on access ports 

output = net_connect.send_command('SHOW MAC ADDRES vlan ' + User_Vlan)
lines = output.splitlines()[6:]

for line in lines:
	words = line.split()
	port = words[2]

	for j in words:
		if j == port and  port != '0' and port not in trunks:
			mac_addr = words[1].lower()
			mac_addr = mac_addr.split(':')
			oui = ''.join(mac_addr[:3])
			for i in dell:
				if i == oui:
					print('Device on ' + port + ' is a Dell PC')
					config.append('Interface ' + port)
					config.append(' description DELL-PC')
					config.append('!')
				else:
					pass
		else:
			pass

net_connect.disconnect()
		
