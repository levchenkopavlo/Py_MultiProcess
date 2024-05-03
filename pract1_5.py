import multiprocessing as mp
import time


def print_info(info):
    for _ in range(10):
        print(info)
        time.sleep(0.5)


def sort_array(arr):
    for _ in range(10):
        print(sorted(arr))
        time.sleep(0.5)


if __name__ == "__main__":
    # mp.freeze_support() # for Windows

    print("Max number of processes", mp.cpu_count())

    p1 = mp.Process(target=print_info, args=("Process 1",))
    p2 = mp.Process(target=sort_array, args=([1, 3, 6, 5, 3, 2],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()