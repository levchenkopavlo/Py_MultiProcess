## Server
import socket

server = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )
server.bind(('127.0.0.1', 5001))
server.listen(2)
print("Waiting...")

client, address = server.accept()
print(f"Connection from {address}")
while True:
    msg = client.recv(1024).decode()
    if msg == 'exit':
        client.close()
        break
    print(msg)
