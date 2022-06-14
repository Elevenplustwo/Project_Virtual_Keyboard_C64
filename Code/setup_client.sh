#!/bin/bash
#!/usr/bin/expect -f
#set pass "test"

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt install -y python-pip #Installiert pip

sudo apt-get install -y git #Installiert git um Dateien von Github zu laden

sudo mkdir -p /home/pi/virtual_keyboard/client
sudo mkdir -p /home/pi/virtual_keyboard/client/Img
sudo chmod 777 -R /home/pi/virtual_keyboard/client/Img

sudo wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/Elevenplustwo/Project_Virtual_Keyboard_C64/main/Code/bluetooth_client.py -P /home/pi/virtual_keyboard/client
sudo wget https://github.com/Elevenplustwo/Project_Virtual_Keyboard_C64/tree/main/Code/Img -P /home/pi/virtual_keyboard/client/Img
#sudo git clone https://github.com/Elevenplustwo/Project_Virtual_Keyboard_C64/blob/main/Code/bluetooth_client.py /home/pi/virtual_keyboard/client/bluetooth_client.py
#sudo git clone https://github.com/Elevenplustwo/Project_Virtual_Keyboard_C64/tree/main/Code/Img /home/pi/virtual_keyboard/client/Img

sudo pip install pybluez #Installiert pybluez
sudo apt-get install libbluetooth-dev #Lädt BT Lib

sudo python3 /home/pi/virtual_keyboard/client/bluetooth_client.py



