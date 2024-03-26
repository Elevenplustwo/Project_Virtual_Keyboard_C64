from bluetooth import *
s = BluetoothSocket(RFCOMM)
ssid="00:21:13:05:A1:D3"
s.connect((ssid,1))
s.send("(0,HIGH)")
s.close()
