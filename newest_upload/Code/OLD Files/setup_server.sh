#!/bin/bash
#!/usr/bin/expect -f
#set pass "test"

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt install -y python -pip #Installiert pip
sudo apt install -y python3 -pip

sudo apt-get install -y git #Installiert git um Dateien von Github zu laden

sudo mkdir -p /home/pi/virtual_keyboard/server
sudo chmod 777 -R /home/pi/virtual_keyboard/server

sudo wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/Elevenplustwo/Project_Virtual_Keyboard_C64/main/Code/bluetooth_server.py -P /home/pi/virtual_keyboard/client

sudo apt install python3-bluez
sudo pip install pybluez #Installiert pybluez
sudo apt-get install libbluetooth-dev #Lädt BT Lib

sudo python3 /home/pi/virtual_keyboard/client/bluetooth_server.py