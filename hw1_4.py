# Завдання 4
# Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
# потоки. Перший потік має знайти файли з потрібним словом і злити їх вміст в один файл.
# Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
# заборонених слів (список цих слів потрібно зчитати з файлу із забороненими словами) з отриманого файлу.
# Виведіть статистику виконаних операцій на екран.
import json
import os
import threading
import datetime


def file_search(source, search_word):
    if source == '':
        source = os.getcwd()
    print('curdir', source)
    for item in os.listdir(source):

        path = os.path.join(source, item)
        print('path', path)
        if os.path.isdir(path):
            file_search(path, search_word)
        else:
            with open(path, 'r', encoding="utf-8") as file:
                data = file.readlines()
            for line in data:
                if search_word in line:
                    with open('result.txt', 'a', encoding="utf-8") as file:
                        file.writelines(data)
                        break


def del_forbidden_words():
    with open('forbidden_words.txt', 'r', encoding="utf-8") as file:
        forbidden_words = file.readlines()

    with open('result.txt', 'r', encoding="utf-8") as file:
        data = file.readlines()
        new_data = []
    for line in data:
        for word in forbidden_words:
            if word in line:
                line = line.replace(word, '')
        new_data.append(line)
    with open('result.txt', 'a', encoding="utf-8") as file:
        file.writelines(new_data)

if __name__ == "__main__":
    source = 'C:\\temp\\test_folder'
    search_word = 'word'

    start_thr1 = datetime.datetime.now().timestamp()
    thread1 = threading.Thread(target=file_search, args=(source, search_word))
    thread1.start()
    thread1.join()
    print(f'search took {datetime.datetime.now().timestamp() - start_thr1} s')

    start_thr2 = datetime.datetime.now().timestamp()
    thread2 = threading.Thread(target=del_forbidden_words, args=())
    thread2.start()
    thread2.join()
    print(f'deleting forbidden words took {datetime.datetime.now().timestamp() - start_thr2} s')
    print(f'total time: {datetime.datetime.now().timestamp() - start_thr1} s')
