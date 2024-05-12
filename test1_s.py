# Завдання 1
# Реалізуйте клієнт-серверний додаток, що дозволяє двом
# користувачам грати в гру «Хрестики — нулики». Один із
# гравців ініціює гру. Якщо другий гравець підтверджує, то
# гра починається. Гру можна припинити. Той хто припинив
# гру — програв. Після завершення гри можна ініціювати повторний матч
## Server

import socket


def print_field(field):
    line1 = f" --- --- ---\n"
    line2 = f"| {field[1]} | {field[2]} | {field[3]} |\n"
    line4 = f"| {field[4]} | {field[5]} | {field[6]} |\n"
    line6 = f"| {field[7]} | {field[8]} | {field[9]} |\n"
    line9 = f" --- --- ---"
    result_line = line1 + line2 + line1 + line4 + line1 + line6 + line9
    print(result_line)
    client.send(result_line.encode())

    # print(f" --- --- ---")
    # print(f"| {field[1]} | {field[2]} | {field[3]} |")
    # client.send(f" --- --- ---\n| {field[1]} | {field[2]} | {field[3]} |\n --- --- ---\n".encode())

    # print(f" --- --- ---")
    # print(f"| {field[4]} | {field[5]} | {field[6]} |")
    # client.send(f"| {field[4]} | {field[5]} | {field[6]} |\n --- --- ---\n".encode())
    #
    # print(f" --- --- ---")
    # print(f"| {field[7]} | {field[8]} | {field[9]} |")
    # print(f" --- --- ---")
    # client.send(f"| {field[7]} | {field[8]} | {field[9]} |\n --- --- ---\n".encode())


sign = ['X', 'O']
sign_to_print = ['\033[34mX\033[0m', '\033[31mO\033[0m']
# field = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
# field_to_print = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
turn = 0
players = ['', '']

server = socket.socket(socket.AF_INET,  # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )

server.bind(('127.0.0.1', 8080))
server.listen(1)

while True:
    while True:
        name = input("Enter your name: ")
        if name:
            players[1] = name
            break
        else:
            print('Name can not be empty.')
            continue

    print("Waiting...")

    client, address = server.accept()
    print(f"Connection from {address}")

    data = client.recv(1024).decode()
    print(f'Player {data} connected')
    players[0] = data
    response = f'Player {players[1]} connected'
    client.send(response.encode())

    while True:
        game_over = False
        field = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        field_to_print = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        turn = 0
        while turn < 9:
            print_field(field_to_print)

            print(f"{turn + 1}. Хід гравця: \033[33m{players[turn % 2]}\033[0m ({sign_to_print[turn % 2]})")
            client.send(f"Хід гравця: \033[33m{players[turn % 2]}\033[0m ({sign_to_print[turn % 2]})\n".encode())
            while True:
                try:
                    if turn % 2:
                        choice = int(input("введіть номер поля для ходу: "))
                    else:
                        client.send("введіть номер поля для ходу: ".encode())
                        choice = int(client.recv(1024).decode())
                    if 0 <= choice <= 9 and field[choice] != 'X' and field[choice] != '0':
                        field[choice] = sign[turn % 2]
                        field_to_print[choice] = sign_to_print[turn % 2]
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("помилка вводу даних")
                    continue
            if field[1] == field[2] == field[3] or field[4] == field[5] == field[6] or field[7] == field[8] == field[
                9] or \
                    field[1] == field[4] == field[7] or field[2] == field[5] == field[8] or field[3] == field[6] == \
                    field[9] or \
                    field[1] == field[5] == field[9] or field[1] == field[5] == field[7]:
                print_field(field_to_print)

                print(f"\033[32mПеремога за \033[33m{players[turn % 2]}\033[32m!\033[0m")
                client.send(f"\033[32mПеремога за \033[33m{players[turn % 2]}\033[32m!\033[0m".encode())
                client.send(f"Гру завершено".encode())
                game_over = True
                break
            turn += 1
        if turn == 9:
            print_field(field_to_print)
            print(f"\033[32mНічия!\033[0m")
            client.send(f"\033[32mНічия!\033[0m".encode())
            client.send(f"Гру завершено".encode())
            game_over = True
        if game_over:
            data = client.recv(1024).decode()
            if data == 'exit':
                break
            else:
                print('continue')
                # new_game=True
                continue

    client.close()
    # server.listen(1)
