import zmq
import asyncio



class Server:

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)

    def bind(self, port):
        self.socket.bind(f"tcp://*:{port}")

    async def received_message(self):
        message_bit = self.socket.recv()
        message_utf8 = message_bit.decode('utf-8')
        return message_utf8

    def send_message(self, message):
        message_bit = message.encode('utf-8')
        self.socket.send(message_bit)


async def main():
    server = Server()
    server.bind(port=4554)

    while True:
        message = await server.received_message()
        print(message)
        server.send_message("Thank You")

asyncio.run(main())