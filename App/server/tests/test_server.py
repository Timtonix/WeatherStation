import pytest
import zmq


class ServerTest:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
    def fake_client(self):
        self.socket.connect('tcp://localhost:4554')

    def test_received_message(self):
        ServerTest.fake_client()
        assert self.socket.send(b'Hello') == "Thank you"



