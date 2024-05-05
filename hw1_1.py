# Завдання 1
# При старті додатку запускаються три потоки. Перший
# потік заповнює список випадковими числами. Два інші потоки
# очікують на заповнення. Коли перелік заповнений, обидва
# потоки запускаються. Перший потік знаходить суму елементів
# списку, другий потік знаходить середнє арифметичне значення
# у списку. Отриманий список, сума та середнє арифметичне
# виводяться на екран.
import threading
import random
import datetime


def random_list(size=100000, limit=9000000):
    global lst
    lst = [random.randint(0, limit) for _ in range(size)]


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
