# Networking
These are scripts and or "how tos" that I have found and/or created to refer back.
# How to install Ansible:
apt-get update

apt-get install software-properties-common

apt-add-repository ppa:ansible/ansible

press "enter" to confirm the addition of repository

apt-get update

apt-get install ansible

# How to install Paramiko or Netmiko:
apt-get update

apt-get install python -y

apt-get install build-essential libssl-dev libffi-dev -y

apt-get install python-pip -y

pip install cryptography

pip install paramiko
or
pip install netmiko

#Install Netmiko for Python 3
sudo apt-get update -y

sudo apt-get install -y python3-netmiko
