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


def random_list(size=100000, limit=9000000):
    # global lst
    lst = [random.randint(0, limit) for _ in range(size)]
    with open(f'random_data.json', 'w', encoding="utf-8") as file:
        json.dump(lst, file)


def get_summ(data):
    global summ
    summ = sum(data)
    # time.sleep(0.5) № artificial delay
    return summ


def get_avg(data):
    global avg
    avg = get_summ(data) / len(data)


if __name__ == "__main__":
    # lst = []
    # summ = 0

    start_thr1 = datetime.datetime.now().timestamp()
    thread1 = threading.Thread(target=random_list, args=(900000,))
    thread1.start()
    thread1.join()
    print(f'the generation of the random list took {datetime.datetime.now().timestamp() - start_thr1} s')

    start_thr2 = datetime.datetime.now().timestamp()
    thread2 = threading.Thread(target=get_summ, args=(lst,))
    start_thr3 = datetime.datetime.now().timestamp()
    thread3 = threading.Thread(target=get_avg, args=(lst,))

    thread2.start()
    thread3.start()

    thread2.join()
    print(summ)
    print(f'summ calculating took {datetime.datetime.now().timestamp() - start_thr2} s')
    thread3.join()
    print(avg)
    print(f'average calculating took {datetime.datetime.now().timestamp() - start_thr3} s')
    print(f'total time: {datetime.datetime.now().timestamp() - start_thr1} s')
