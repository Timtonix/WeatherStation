import socket
from temperature import *
import json
import time

"""
    Setup :
    -Socket
    -Temperature/DHTSensor
"""
setup_dht_sensor()
client = socket.socket()
is_connected = False


while not is_connected:
    try:
        client.connect(('192.168.1.103', 4554))
        is_connected = True
    except OSError:
        print("Can't connect")
        is_connected = False
        time.sleep(5)

response = "Ok"
# Send request and receive response
while response != "QUIT":
    json_message = {'temp': get_temperature(), 'humidity': get_humidity()}
    print(json_message)
    client.send(json.dumps(json_message).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(response)
    time.sleep(300)

client.close()


my_dict = {"temp": 23, "humidity": 154}
client.socket.send(json.dumps(my_dict).encode('utf-8'))
