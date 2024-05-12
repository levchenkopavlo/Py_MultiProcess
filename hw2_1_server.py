# Завдання 1
# Реалізуйте клієнт-серверний додаток, що дозволяє двом
# користувачам грати в гру «Хрестики — нулики». Один із
# гравців ініціює гру. Якщо другий гравець підтверджує, то
# гра починається. Гру можна припинити. Той хто припинив
# гру — програв. Після завершення гри можна ініціювати повторний матч
## Server
import socket
import threading
import random
import time


def client_login():
    print('waiting for client')
    client, address = server.accept()
    print(f"Connection from {address}")
    name = client.recv(1024).decode()
    clients[name] = client
    for key, value in clients.items():
        print(f'{key}: {value}')
    client.send(f'Player {name} connected'.encode())
    print(f'Player {name} connected')


def client_logout():
    pass


def send_msg(msg):
    for client in clients.values():
        client.send(msg.encode())


def print_field(field):
    line1 = f" --- --- ---\n"
    line2 = f"| {field[1]} | {field[2]} | {field[3]} |\n"
    line4 = f"| {field[4]} | {field[5]} | {field[6]} |\n"
    line6 = f"| {field[7]} | {field[8]} | {field[9]} |\n"
    # line7 = f" --- --- ---"

    sum_line = line1 + line2 + line1 + line4 + line1 + line6 + line1
    print(sum_line)
    send_msg(sum_line)


def game():
    turn = 0

    while turn < 9:
        print_field(field_to_print)
        time.sleep(0.1)
        # print(f"Хід гравця: \033[33m{players[turn % 2]}\033[0m ({sign_to_print[turn % 2]})")
        send_msg(f"Хід гравця: \033[33m{players[turn % 2]}\033[0m ({sign_to_print[turn % 2]})")
        while True:
            try:
                # choice = int(input("введіть номер поля для ходу: "))
                send_msg('system' + players[turn % 2])
                choice = int(clients[players[turn % 2]].recv(1024).decode('utf-8'))
                if 0 <= choice <= 9 and field[choice] != 'X' and field[choice] != '0':
                    field[choice] = sign[turn % 2]
                    field_to_print[choice] = sign_to_print[turn % 2]
                    break
                else:
                    raise ValueError
            except ValueError:
                print("помилка вводу даних")
                continue
        if field[1] == field[2] == field[3] or field[4] == field[5] == field[6] or field[7] == field[8] == field[9] or \
                field[1] == field[4] == field[7] or field[2] == field[5] == field[8] or field[3] == field[6] == field[
            9] or \
                field[1] == field[5] == field[9] or field[1] == field[5] == field[7]:
            print_field(field_to_print)
            print(f"\033[32mГру завершено. Перемога за: \033[33m{players[turn % 2]}\033[32m.\033[0m")
            send_msg(f"\033[32mГру завершено. Перемога за: \033[33m{players[turn % 2]}\033[32m.\033[0m")
            break
        turn += 1
    if turn == 9:
        print_field(field_to_print)
        print(f"\033[32mНічия!\033[0m")
        send_msg(f"\033[32mНічия!\033[0m")


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET,  # use IP4
                           socket.SOCK_STREAM  # use TCP
                           )
    server.bind(('127.0.0.1', 6000))
    server.listen(2)
    clients = {}

    thread_login_player1 = threading.Thread(target=client_login, args=())
    thread_login_player1.start()
    thread_login_player2 = threading.Thread(target=client_login, args=())
    thread_login_player2.start()
    thread_login_player1.join()
    thread_login_player2.join()

    players = random.sample(list(clients.keys()), 2)
    sign = ['X', 'O']
    sign_to_print = ['\033[34mX\033[0m', '\033[31mO\033[0m']
    field = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    field_to_print = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    game()
