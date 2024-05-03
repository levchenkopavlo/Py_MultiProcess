import threading


def print_info(info):
    for _ in range(10):
        print(info)


def sort_array(arr):
    for _ in range(10):
        print(sorted(arr))


t1 = threading.Thread(target=print_info, args=("Thread1",))
t2 = threading.Thread(target=sort_array, args=([2, 3, 1, 5, 4],))

t1.start()
t2.start()

t1.join()
t2.join()