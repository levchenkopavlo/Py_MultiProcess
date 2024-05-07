# Завдання 1
# Реалізуйте гру "Хрестики-Нулики" для двох гравців.
# Використовуйте словник для представлення гри.
def get_player_names(count=None):
    names = []
    counter = 1
    while True:
        if count:
            if counter <= count:
                name = input(f"Ведіть ім'я гравця №{counter}: ")
                if not name:
                    continue
                else:
                    names.append(name)
                    counter += 1
            else:
                break
        else:
            name = input(f"Ведіть ім'я гравця №{counter} (Enter, щоб завершити): ")
            if not name:
                break
            else:
                names.append(name)
                counter += 1

    return names


def print_field(field):
    print(f" --- --- ---")
    print(f"| {field[1]} | {field[2]} | {field[3]} |")
    print(f" --- --- ---")
    print(f"| {field[4]} | {field[5]} | {field[6]} |")
    print(f" --- --- ---")
    print(f"| {field[7]} | {field[8]} | {field[9]} |")
    print(f" --- --- ---")


players = get_player_names(2)
sign = ['X', 'O']
sign_to_print = ['\033[34mX\033[0m', '\033[31mO\033[0m']
field = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
field_to_print = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
turn = 0
while turn < 9:
    print_field(field_to_print)
    print(f"Хід гравця: \033[33m{players[turn % 2]}\033[0m ({sign_to_print[turn % 2]})")
    while True:
        try:
            choice = int(input("введіть номер поля для ходу: "))
            if 0 <= choice <= 9 and field[choice] != 'X' and field[choice] != 'Y':
                field[choice] = sign[turn % 2]
                field_to_print[choice] = sign_to_print[turn % 2]
                break
            else:
                raise ValueError
        except ValueError:
            print("помилка вводу даних")
            continue
    if field[1] == field[2] == field[3] or field[4] == field[5] == field[6] or field[7] == field[8] == field[9] or \
            field[1] == field[4] == field[7] or field[2] == field[5] == field[8] or field[3] == field[6] == field[9] or \
            field[1] == field[5] == field[9] or field[1] == field[5] == field[7]:
        print_field(field_to_print)
        print(f"\033[32mВітаю \033[33m{players[turn % 2]}\033[32m, Ви перемогли!\033[0m")
        break
    turn += 1
if turn == 9:
    print_field(field_to_print)
    print(f"\033[32mНічия!\033[0m")