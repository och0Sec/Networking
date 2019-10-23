# Networking
These are scripts and or "how tos" that I have found and/or created to refer back.
# How to install Ansible:
apt-get update

apt-get install software-properties-common

apt-add-repository ppa:ansible/ansible

press "enter" to confirm the addition of repository

apt-get update -y

apt-get dist-upgrade -y

reboot

apt-get install ansible

# How to install Paramiko or Netmiko:
apt-get update -y

apt-get dist-upgrade -y

reboot

apt-get install python 

apt-get install build-essential libssl-dev libffi-dev 

apt-get install python-pip 

pip install cryptography 

pip install simple-crypt 

pip install pycrypto 

pip install paramiko 
or
pip install netmiko 

# Install Netmiko for Python 3
sudo apt-get update -y

sudo apt-get dist-upgrade -y

reboot

apt-get install python3 

apt-get install  python3-netmiko or after installing pip3: pip3 install netmiko

apt-get install python3-pip 

pip3 install cryptography 

pip3 install simple-crypt 

pip3 install pycrypto 
