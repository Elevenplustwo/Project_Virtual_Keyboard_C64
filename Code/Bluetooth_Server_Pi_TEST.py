from bluetooth import *
s = BluetoothSocket(RFCOMM)
ssid="00:21:13:05:A1:D3"
psk="1234"
s.connect((ssid,1))
data=[ssid,psk]
s.send("(0,HIGH)")
s.close()
