# import socket programming library
import socket
from collect_json import *
import threading


def process_client(client):
    while True:
        request = client.recv(1024)
        request = request.decode('utf-8')
        print(request)
        if not request:
            print(">Client has disconnected")
            break
        message = "Continue"
        message = message.encode('utf-8')

        try:
            request = json.loads(request)
            collect_json.main(request)
            client.send(message)
        except ValueError:
            print(">Client send a false JSON")
            message = "QUIT"
            message = message.encode('utf-8')
            client.send(message)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 4554))
socket.listen(1)
print(">I'm listening")
collect_json = CollectJson()

while True:
    print(">Waiting for a client")
    client, address = socket.accept()
    print(f"Connect with {address}")
    request = threading.Thread(target=process_client, args=(client,))
    request.start()
    print(">Before request.join()")
    request.join()
    print(">Finish all the code")

