# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.

import threading
import random
import datetime
import json


def odd_to_file(file_name):
    start = datetime.datetime.now().timestamp()
    with open(file_name, 'r', encoding="utf-8") as file:
        data = json.load(file)
    new_data = [number for number in data if number % 2]
    with open(f'odd_data.json', 'w', encoding="utf-8") as file:
        json.dump(new_data, file)
    print(f'write odd numbers: {datetime.datetime.now().timestamp() - start}s')
    print()


def even_to_file(file_name):
    start = datetime.datetime.now().timestamp()
    with open(file_name, 'r', encoding="utf-8") as file:
        data = json.load(file)
    new_data = [number for number in data if not number % 2]
    with open(f'even_data.json', 'w', encoding="utf-8") as file:
        json.dump(new_data, file)
    print(f'write even numbers: {datetime.datetime.now().timestamp() - start}s')


if __name__ == "__main__":
    # user_list = [random.randint(0, 9000000) for _ in range(100000)]
    #
    # with open(f'random_data.json', 'w', encoding="utf-8") as file:
    #     json.dump(user_list, file)

    start = datetime.datetime.now().timestamp()
    thread1 = threading.Thread(target=odd_to_file, args=('random_data.json',))
    thread2 = threading.Thread(target=even_to_file, args=('random_data.json',))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print()
    print(f'summary time {datetime.datetime.now().timestamp() - start}s')
