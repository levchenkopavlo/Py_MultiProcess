## Server


import socket
import translators as ts


def translate(text, src='uk', dest='en'):
    try:
        translation = ts.translate_text(text, from_language=src, to_language=dest)
        return translation
    except Exception as e:
        return "translate error"


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

        if data == 'exit':
            break

        response = translate(data, 'uk', 'en')

        client.send(response.encode())

    client.close()
