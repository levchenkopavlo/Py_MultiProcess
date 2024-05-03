import queue
import threading
import time


def worker(thread_num):
    global tasks

    while True:
        task = tasks.get()

        if task is None:
            break

        print(f"Thread №{thread_num} work with {task}\n", end='')
        tasks.task_done()
        time.sleep(0.5)


tasks = queue.Queue()
num_threads = 3

for i in range(10):
    tasks.put(f"Task {i+1}")

for _ in range(num_threads):
    tasks.put(None)

threads = []
for i in range(num_threads):
    t = threading.Thread(target=worker, args=(i+1,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()