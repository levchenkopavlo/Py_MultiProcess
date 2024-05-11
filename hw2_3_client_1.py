## Client

import socket
import threading


def msg_send():
    pass


def msg_receive():
    pass


if __name__ == "__main__":

    client = socket.socket(socket.AF_INET,  # use IP4
                           socket.SOCK_STREAM  # use TCP
                           )

    client.connect(('127.0.0.1', 8080))

    while True:
        data = input("Enter something: ")

        client.send(data.encode())

        if data == 'exit':
            break

        response = client.recv(1024).decode()
        print(response)

    client.close()

    thread_send = threading.Thread(target=None, args=())
    thread_send.start()

    thread_receive = threading.Thread(target=None, args=())
    thread_receive.start()

    thread_send.join()
    thread_receive.join()
