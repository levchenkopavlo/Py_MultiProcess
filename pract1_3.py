import threading


global_list = []
lock = threading.Lock()


def append():
    for _ in range(100000):
        global global_list

        lock.acquire()
        global_list.append(1)
        lock.release()


def remove():
    for _ in range(100000):
        global global_list

        lock.acquire()
        global_list.pop()
        lock.release()


t1 = threading.Thread(target=append, args=())
t2 = threading.Thread(target=remove, args=())

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final result {global_list}")