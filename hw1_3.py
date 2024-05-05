# Завдання 3
# Користувач вводить з клавіатури шлях до існуючої та
# до нової директорії. Після чого запускається потік, який має
# скопіювати вміст директорії у нове місце. Збережіть структуру
# директорії. Виведіть статистику виконаних операцій на екран.
import os
import shutil
import threading
import datetime


def copy_dir(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        path_from = os.path.join(source, item)
        path_to = os.path.join(destination, item)
        if os.path.isdir(path_from):
            copy_dir(path_from, path_to)
        else:
            shutil.copy(path_from, path_to)


# def copy_dir2(source, destination):
#     try:
#         shutil.copytree(source, destination)
#     except Exception as e:
#         print(f"Copying error: {e}")

if __name__ == "__main__":
    source = 'c:\\temp\\driver'
    destination = 'c:\\temp1'
    start_thr1 = datetime.datetime.now().timestamp()
    thread1 = threading.Thread(target=copy_dir, args=(source, destination))
    thread1.start()
    thread1.join()
    print(f'directory copying took {datetime.datetime.now().timestamp() - start_thr1} s')

