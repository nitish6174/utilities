## Server setup

Common installations on a new machine/server


```bash
# --------------------------------------------------
# apt commands
# --------------------------------------------------
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get autoclean
# --------------------------------------------------
# Basic programs
# --------------------------------------------------
sudo apt-get install vim
sudo apt-get install git
sudo apt-get install curl
sudo apt-get install openssh-server
# --------------------------------------------------
# Python
# --------------------------------------------------
sudo apt-get install python3 python3-pip python3-dev
# Python virtual environment
pip3 install virtualenv
# Alternative to pip: sudo apt-get install python3-virtualenv
# --------------------------------------------------
# Apache, PHP
# --------------------------------------------------
sudo apt-get install apache2 apache2-utils
sudo apt-get install php7.0 libapache2-mod-php7.0
# --------------------------------------------------
# Databases
# --------------------------------------------------
# MySQL basic
sudo apt-get install mysql-client mysql-server
# For running MySQL with Python / Advanced usage
sudo apt-get install libmysqlclient-dev
# GUI for MySQL
sudo apt-get install mysql-workbench
# MongoDB
sudo apt-get install mongodb
# Install RoboMongo - GUI for MongoDB
# --------------------------------------------------
# To run VPN client
# --------------------------------------------------
sudo apt-get install openvpn
```
