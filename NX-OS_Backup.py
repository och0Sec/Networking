#!/usr/bin/env python3
from netmiko import ConnectHandler
import get_nxos_creds
import datetime
import os

def backup():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")

    USER,PASSWORD = get_nxos_creds.decrypt()

    #Replace the IPs below with your MDS switches IPs:
    Switches=['192.168.1.2', '192.168.1.3']

    path = "/backups"
    
    for ip in Switches:
        switch_d = {'device_type': 'cisco_nxos', 'ip': ip, 'username': USER, 'password': PASSWORD}
        ssh_session = ConnectHandler(**switch_d)
        filename = "NX-OS_" + date + "_" + ip + '.bak'
        fullpath = os.path.join(path,filename)
        showrun = ssh_session.send_command('show run')
        file = open(fullpath, "w")
        file.write(showrun)
        file.close()
        ssh_session.disconnect()
