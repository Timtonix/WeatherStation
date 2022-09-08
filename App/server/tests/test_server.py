import pytest
import zmq


class TestServer:
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    def fake_client(self):
        TestServer.socket.connect('tcp://localhost:4554')

    def test_received_message(self):
        self.fake_client()
        TestServer.socket.send(b'Hello')
        response = TestServer.socket.recv()
        assert response == b'Thank You'



