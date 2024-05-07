## Client

import socket

client = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )

client.connect(('127.0.0.1', 8080))

while True:
    name = input("Enter your name: ")
    if name:
        break
    else:
        print('Name can not be empty.')
        continue
client.send(name.encode())
while True:
    response = client.recv(1024).decode()
    print(response)
    if response == "введіть номер поля для ходу: ":
        client.send(input().encode())
    if response == "Гру завершено":
        answer = input("Введіть exit для виходу або натисніть Enter для продовження: ")
        client.send(input().encode())
        if answer == 'exit':
            client.close()



# if name == 'exit':
#     break
