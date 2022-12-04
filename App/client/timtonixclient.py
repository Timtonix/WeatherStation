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
import network
import socket
import dht
import machine
import json
import time

d = dht.DHT11(machine.Pin(4))
client = socket.socket()
is_connected = False
while is_connected != True:
    try:
        client.connect(('192.168.1.103', 4554))
        is_connected = True
    except OSError:
        print("Can't connect")
        is_connected = False
        time.sleep(5)
flag = 0

while flag == 0:
    try:
        d.measure()
        print("It's work !")
        flag = 1
    except OSError:
        flag = 0
        print("Something wrong with d.measure()")

response = "Ok"

while response != "QUIT":
    json_message = {'temp': d.temperature(), 'humidity': d.humidity()}
    print(json_message)
    client.send(json.dumps(json_message).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(response)
    time.sleep(300)

client.close()
