import json
import socket
import asyncio
from collect_json import *


class Server:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, port):
        self.socket.bind(("", port))
        self.socket.listen()
        self.conn , self.addr = self.socket.accept()

    async def received_message(self):
        message_bit = self.conn.recv(1024)
        message_utf8 = message_bit.decode('utf-8')
        return message_utf8

    def send_message(self, message):
        message_bit = message.encode('utf-8')
        self.conn.send(message_bit)


async def main():
    server = Server()
    server.bind(port=4554)
    # Create the collect_json object
    collect_json = CollectJson()

    while True:
        message = await server.received_message()
        print(f"Connect with {server.addr}")
        print(message)
        try:
            message = json.loads(message)
            collect_json.main(message)
        except ValueError:
            server.send_message("QUIT")
        server.send_message("Ok")

asyncio.run(main())
