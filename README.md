# Networking
These are scripts and or "how tos" that I have found and/or created to refer back.
# How to install Ansible:
apt-get update

apt-get install software-properties-common

apt-add-repository ppa:ansible/ansible

press "enter" to confirm the addition of repository

apt-get update

apt-get dist-upgrade -y 

reboot

apt-get install ansible

# How to install Paramiko or Netmiko:
apt-get update -y

apt-get dist-upgrade -y

reboot

apt-get install python -y

apt-get install build-essential libssl-dev libffi-dev -y

apt-get install python-pip -y

pip install cryptography -y

pip install simple-crypt -y

pip install pycrypto -y

pip install paramiko -y
or
pip install netmiko -y

# Install Netmiko for Python 3
sudo apt-get update -y

sudo apt-get dist-upgrade -y

reboot

sudo apt-get install -y python3-netmiko

apt-get install python3-pip -y

pip3 install cryptography -y

pip3 install simple-crypt -y

pip3 install pycrypto -y
