import socket

PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.20.0.3"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
connected = True

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

def receive():
    while connected:
        data = client.recv(2048).decode(FORMAT)


def main():
    pass

main()