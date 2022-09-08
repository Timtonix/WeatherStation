import zmq
import asyncio



class Client:

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    def connect(self, port):
        self.socket.connect(f"tcp://localhost:{port}")


client = Client()
client.connect(4554)
client.socket.send(b'hello')
print(client.socket.recv())