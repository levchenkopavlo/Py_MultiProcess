# Завдання 2
# Реалізуйте клієнт-серверний додаток з можливістю надсилати файли. Один користувач ініціює надсилання файлу, другий
# підтверджує. Після підтвердження починається надсилання.
# Якщо відправка була вдалою, повідомте про це відправника.

## Server
import socket

server = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )

server.bind(('127.0.0.1', 8080))
server.listen(1)

while True:

    print("Waiting...")

    client, address = server.accept()
    print(f"Connection from {address}")

    while True:
        data = client.recv(1024).decode()
        print(data)

        if data == 'exit':
            break

        response = input("Enter something: ")

        client.send(response.encode())

    client.close()
    server.listen(1)
