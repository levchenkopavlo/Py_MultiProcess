# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
import threading
import random
import datetime


def get_max(data):
    start = datetime.datetime.now().timestamp()
    print(max(data))
    print(f'search for the maximum {datetime.datetime.now().timestamp() - start}s')


def get_min(data):
    start = datetime.datetime.now().timestamp()
    print(min(data))
    print(f'search for the minimum {datetime.datetime.now().timestamp() - start}s')


if __name__ == "__main__":
    # user_list = list(map(int, input(f'input integer numbers space separated:').split()))
    user_list = [random.randint(0, 9000000) for _ in range(100000)]

    start = datetime.datetime.now().timestamp()
    thread1 = threading.Thread(target=get_max, args=(user_list,))
    thread2 = threading.Thread(target=get_min, args=(user_list,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(f'summary time {datetime.datetime.now().timestamp() - start}s')