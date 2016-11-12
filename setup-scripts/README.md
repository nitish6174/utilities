## Server setup

Common installations on a new machine/server


```bash
sudo apt-get update
sudo apt-get upgrade
# --------------------------------------------------
# Basic programs
# --------------------------------------------------
sudo apt-get install openssh-server
sudo apt-get install vim
sudo apt-get install git
sudo apt-get install curl
# --------------------------------------------------
# Python
# --------------------------------------------------
sudo apt-get install python python-pip python-dev
# Python virtual environement
pip install virtualenv
# Alternative to pip: sudo apt-get install python-virtualenv
# --------------------------------------------------
# Apache, PHP and MySQL
# --------------------------------------------------
sudo apt-get install apache2 apache2-utils
sudo apt-get install php7.0 libapache2-mod-php7.0
sudo apt-get install mysql-client mysql-server
# --------------------------------------------------
# To run VPN client
# --------------------------------------------------
sudo apt-get install openvpn
# --------------------------------------------------
# Python modules
# --------------------------------------------------
# Python numpy library
pip install numpy
# Alternative to pip: sudo apt-get install python-numpy
# Python Flask framework
pip install flask
pip install requests
```