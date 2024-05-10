# Завдання 2
# Реалізуйте клієнт-серверний додаток з можливістю надсилати файли. Один користувач ініціює надсилання файлу, другий
# підтверджує. Після підтвердження починається надсилання.
# Якщо відправка була вдалою, повідомте про це відправника.
## Server
import socket

server = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )
server.bind(('127.0.0.1', 5000))
server.listen(2)
print("Waiting...")

client, address = server.accept()
print(f"Connection from {address}")
data = client.recv(1024).decode()
while True:
    accept = input(f'Receive file {data} (y/n)? ')
    if accept.lower() == 'y':
        client.send('y'.encode())

        file_size = int(client.recv(1024).decode())
        with open('incoming.txt', 'wb') as file:
            receive = 0
            while receive < file_size:
                data = client.recv(1024)
                file.write(data)
                receive += len(data)

        client.send(f'File received'.encode())

        break
    elif accept.lower() == 'n':
        client.send('n'.encode())
        break
    else:
        continue
client.close()
