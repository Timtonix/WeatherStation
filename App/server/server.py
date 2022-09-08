import zmq


class Server:

    def __init__(self):
        self.context = zmq.Context
        self.socket = self.context.socket(zmq.REP)

    def bind(self, ip, port):
        self.socket.bind(f"{ip}:{port}")



