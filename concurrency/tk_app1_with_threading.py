'''
Код повторяет приложение tk_app1.py
Но теперь дополняется многопоточностью, за счет добавления одноименного модуля
Моделирование работы sleep_func запускается в новом потоке


Мультипоточность применяется для решения множества легких задач, когда необходимо много ожидания
Решает задачи: множество сетевых запросов, например к базе данных, обращение к API сервера или операции I/O
В таких задачах код исполняется быстро, например, отправляя запрос, но с требованием ожидания по времени, для получения ответа.
'''

import tkinter as tk
from tkinter import ttk
import time
import threading


def sleep_func():
    time.sleep(10)
    lab['text'] = 'Прошло 10 секунд\nЗадача выполнена в новом потоке'

def start_sleep_thread():
    '''Добавление функции по обработке мультипотоков'''
    thread = threading.Thread(target=sleep_func)
    thread.start()

root = tk.Tk()
root.geometry('300x300+150+150')

btn = ttk.Button(root, text='Run', command=start_sleep_thread)  # Многопоточное выполнение. Функции start_sleep_thread запускается в отдельном потоке
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text='Текст до нажатия')
lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)




if __name__ == '__main__':
    root.mainloop()
