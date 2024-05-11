## Client
import os
import socket

client = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )
client.connect(('127.0.0.1', 5001))

while True:
    msg = input('your message: ')
    client.send(msg.encode())
    if msg == 'exit':
        # client.close()
        break

