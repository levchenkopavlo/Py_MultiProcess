# Завдання 2
# Користувач вводить з клавіатури шлях до файлу. Після
# чого запускаються три потоки. Перший потік заповнює файл
# випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі. Результати пошуку
# кожен потік має записати у новий файл. Виведіть на екран
# статистику виконаних операцій.
import threading
import random
import datetime, time
import json
import math


def random_list(size=10000, limit=90000):
    # global lst
    lst = [random.randint(-limit, limit) for _ in range(size)]
    with open(f'random_data.json', 'w', encoding="utf-8") as file:
        json.dump(lst, file)


def random_list2(size=10000, limit=90000):
    with open(f'random_data.json', 'w', encoding="utf-8") as file:
        for _ in range(size):
            json.dump([random.randint(-limit, limit)], file)
            file.write('\n')


def get_natural(file_name='random_data.json'):
    with open(file_name, 'r', encoding="utf-8") as file:
        data = json.load(file)
    natural_numbers = [num for num in data if num >= 0]
    with open(f'natural_numbers.json', 'w', encoding="utf-8") as file:
        json.dump(natural_numbers, file)


def get_natural2(file_name='random_data.json'):
    with open(file_name, 'r', encoding="utf-8") as file:
        data = file.readlines()
    with open(f'natural_numbers.json', 'w', encoding="utf-8") as file:
        for item in data:
            if json.loads(item.strip())[0] >= 0:
                json.dump(json.loads(item.strip()), file)
                file.write('\n')


def get_factorial(file_name='random_data.json'):
    with open(file_name, 'r', encoding="utf-8") as file:
        data = json.load(file)
    factorials = [math.factorial(num) for num in data if num >= 0]
    with open(f'factorial_numbers.json', 'w', encoding="utf-8") as file:
        json.dump(factorials, file)


def get_factorial2(file_name='random_data.json'):
    with open(file_name, 'r', encoding="utf-8") as file:
        data = file.readlines()
    with open(f'factorial_numbers.json', 'w', encoding="utf-8") as file:
        for item in data:
            number = json.loads(item.strip())[0]
            if number >= 0:
                json.dump(math.factorial(number), file)
                file.write('\n')


if __name__ == "__main__":
    # lst = []
    # summ = 0

    start_thr1 = datetime.datetime.now().timestamp()
    thread1 = threading.Thread(target=random_list2, args=(90000,))
    thread1.start()
    thread1.join()
    print(f'the generation of the random list took {datetime.datetime.now().timestamp() - start_thr1} s')

    start_thr2 = datetime.datetime.now().timestamp()
    thread2 = threading.Thread(target=get_natural2, args=())
    start_thr3 = datetime.datetime.now().timestamp()
    thread3 = threading.Thread(target=get_factorial2, args=())

    thread2.start()
    thread3.start()

    thread2.join()
    print(f'find natural took {datetime.datetime.now().timestamp() - start_thr2} s')
    thread3.join()
    print(f'factorial calculating took {datetime.datetime.now().timestamp() - start_thr3} s')
    print(f'total time: {datetime.datetime.now().timestamp() - start_thr1} s')
