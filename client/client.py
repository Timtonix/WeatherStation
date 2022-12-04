import socket
from temperature import *
import json
import time

"""
    Setup :
    -Socket
    -Temperature/DHTSensor
"""
dht = DHT_sensor(4)
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

response = "Ok"
#Send request and receive response
while response != "QUIT":
    json_message = {'temp': dht.get_temperature(), 'humidity': dht.get_humidity()}
    print(json_message)
    client.send(json.dumps(json_message).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(response)
    time.sleep(10)

client.close()

