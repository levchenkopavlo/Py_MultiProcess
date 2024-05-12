## Client
import socket
import threading


def msg_receive():
    while True:
        msg = client.recv(1024).decode()
        if msg == 'system' + name:
            # print('--- ' + msg)
            # print('--- ' + 'system' + name)
            choice = input("введіть номер поля для ходу: ")
            client.send(choice.encode('utf-8'))
        elif msg.startswith('system'):
            pass
        elif msg:
            print(msg)

        # print('!!!')


def login():
    while True:
        name = input("Enter your name: ")
        if not name:
            print('Name can not be empty.')
            continue
        client.send(name.encode())
        response = client.recv(1024).decode()
        break

    if 'welcome' in response:
        print('You authorized.')
        print(response)
    return name


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET,  # use IP4
                           socket.SOCK_STREAM  # use TCP
                           )
    client.connect(('127.0.0.1', 6000))
    name = login()
    # print(name)

    thread_receive = threading.Thread(target=msg_receive, args=())
    thread_receive.start()
