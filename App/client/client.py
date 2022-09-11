import zmq
import asyncio
import json

class Client:

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    def connect(self, port):
        self.socket.connect(f"tcp://localhost:{port}")

    async def received_message(self):
        message = self.socket.recv()
        message = message.decode('utf-8')


client = Client()
client.connect(4554)

my_dict = {"temp": 23, "humidity": 154}
client.socket.send(json.dumps(my_dict).encode('utf-8'))
