## Client
import os
import socket

client = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )
client.connect(('127.0.0.1', 5000))

file_name = input("Enter filename: ")
# file_name = 'temp.py'
client.send(file_name.encode())

response = client.recv(1024).decode()
# response = 'y'
if response == 'y':
    file_size = os.path.getsize(file_name)
    client.send(str(file_size).encode())
    with open(file_name, 'rb') as file:
        data = file.read(1024)
        while data:
            client.send(data)
            data = file.read(1024)
    response = client.recv(1024).decode()
    print(response)
else:
    print(f'File transfer refused from server')
client.close()
