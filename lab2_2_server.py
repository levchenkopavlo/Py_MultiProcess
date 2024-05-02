## Server

import socket

server = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )

weater = {'kyiv': ['+20', 'хмарно', 'вітер +-'], 'toronto': ['+15', 'сонячно', ''],
          'odesa': ['+25', 'сонячно', 'без вітру']}

server.bind(('127.0.0.1', 8081))
server.listen(1)

while True:
    print("Waiting...")

    client, address = server.accept()
    print(f"Connection from {address}")

    while True:
        data = client.recv(1024).decode()

        if data == 'exit':
            break

        if data.lower() in weater:
            response = f'{weater[data.lower()]}'
        else:
            response = 'City not found'

        client.send(response.encode())

    client.close()
