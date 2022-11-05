"""
Author : Timtonix
Date : 5 Nov. 2022
For : Devlowave JA

What
----
Client module to send temperature and humidity to the server !

Hardware
________
* Nodemcu V3
* DHT11

Software
--------
* Micropython for ESP8266
* DHT11 lib
* Network lib
* Socket
"""
#import network
import socket
#import dht
#import machine

#d = dht.DHT11(machine.Pin(4))
client = socket.socket()
client.connect(('192.168.1.92', 4554))
client.send(b'HELLLLLLOO')
print(client.recv(1024))

"""while True:
    try:
        d.measure()
        print(d.temperature())
    except OSError:
        print("Oops! this crash...")"""