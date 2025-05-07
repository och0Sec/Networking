# och0Sec Networking Toolkit

Welcome to the **och0Sec Networking Toolkit**—your one-stop collection of handy scripts and step-by-step “how-tos” for automating common network tasks and device configurations. Whether you’re backing up device configs, encrypting GRE tunnels, or spinning up Ansible-powered workflows, you’ll find something here to save time and keep your network humming.

---

## 📂 Repository Contents

| Script / Guide                                | Purpose                                                         |
|-----------------------------------------------|-----------------------------------------------------------------|
| **Backup-Config.py3**                         | Connect to devices and archive running configurations.         |
| **NX-OS_Backup.py**                           | Automate backups for Cisco NX-OS platforms.                    |
| **Encrypt GRE Tunnels**                       | Walk-through to encrypt your GRE tunnels end-to-end.           |
| **How to configure DMVPN**                    | Step-by-step DMVPN deployment on Cisco routers.                |
| **Static route with IP SLA and Tracking**     | Keep static routes alive with SLA probes and track statements. |
| **How to upgrade firmware on SG350 Switch**   | GUI and CLI steps to update Cisco SG350 series.               |
| **compress.py**                               | Compress large config files before archiving.                 |
| **configFromFile.py**                         | Push batched configurations from a local file.                |
| **create_mac_file.py**                        | Generate MAC-address inventories for audit or automation.     |
| **find_dell_ports.py**                        | Discover and report active ports on Dell switches.           |
| **get_nxos_creds.py**                         | Safely retrieve NX-OS credentials from vaults or files.       |
| **get_vendor.py**                             | Detect device vendor via SNMP/SSH fingerprinting.             |
| **ios_facts.yml**                             | Ansible playbook to gather IOS device facts.                  |
| **s3xx_test_connect.py**                      | Verify reachability of HP Aruba S3xx series switches.        |
| **sg300_show_port_status.py**                 | Show and parse port status on Cisco SG300 series.            |
| **tftpd-hpa**                                 | Quick “How-to” install of TFTP server on Ubuntu.              |
| **ansible.cfg**                               | Example Ansible configuration for device inventories.         |

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/och0Sec/Networking.git
   cd Networking

2. **Install prerequisites**

   * **Ansible**

     ```bash
     sudo apt update
     sudo apt install software-properties-common
     sudo apt-add-repository --yes --update ppa:ansible/ansible
     sudo apt install ansible

   * **Python 3 + Pip**

     ```bash
     sudo apt update && sudo apt upgrade -y
     sudo apt install python3 python3-pip build-essential libssl-dev libffi-dev

3. **Install network-automation libraries**

   ```bash
   pip3 install paramiko netmiko cryptography simple-crypt pycrypto

4. **Enable TextFSM for structured parsing**

   ```bash
   git clone https://github.com/networktocode/ntc-templates.git
   export NET_TEXTFSM=/path/to/ntc-templates/templates/

5. **Run a script**

   ```bash
   python3 Backup-Config.py3 --inventory hosts.yml --output ./backups

---

## 🛠️ Usage Examples

* **Back up Cisco IOS configs**

  ```bash
  python3 Backup-Config.py3 \
    --hosts ios_devices.yml \
    --username admin \
    --password secret \
    --output ./backups/ios

* **Encrypt a GRE tunnel**
  Follow the interactive prompts:

  ```bash
  python3 Encrypt\ GRE\ Tunnels.py3

  You’ll be guided through key exchange and tunnel parameters.

* **Gather Ansible facts**

  ```bash
  ansible-playbook ios_facts.yml -i hosts.ini

---

## 🤝 Contributing

We welcome improvements, bug fixes, and new automation ideas:

1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/my-script`).
3. Commit your changes (`git commit -m 'Add awesome feature'`).
4. Push to your branch (`git push origin feature/my-script`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use and adapt any part of it—just keep attribution in place.

---

Thanks for checking out **och0Sec Networking Toolkit**! If you find a bug, have a suggestion, or just want to say hi, open an issue or drop a note in the repo. Happy automating! 🚀
