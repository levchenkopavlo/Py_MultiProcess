import multiprocessing as mp


def mean(arr):
    summa = sum(arr)

    return summa / len(arr)


def get_parts(arr, num=mp.cpu_count()):
    n = len(arr)
    part_len = n // num

    return [arr[(part_len*k) : part_len*(k+1)] for k in range(num)]


def get_arr(len=100_000):
    return list(range(len))


if __name__ == '__main__':
    arr = get_arr()
    parts = get_parts(arr)

    with mp.Pool() as pool:
        results = pool.map(func=mean, iterable=parts)

    print(f"Results of pool {results}")

    print(f"Computed mean value {mean(results)}")
    print(f"Real mean value {mean(arr)}")

