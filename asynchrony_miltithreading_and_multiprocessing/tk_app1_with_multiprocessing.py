'''
Код частично повторяет приложение tk_app1.py
Но теперь дополнителяется процессом, за счет добавления одноименного модуля multiprocessing
Моделирование работы new_process запускается в новом процессе


Мультипроцессинг применяется для решения тяжелых задач, когда вся нагрузка ложиться на процессор
Решает задачи: рендер видео, численные расчёты, обработка данных, машинное обучение.
'''

import tkinter as tk
from tkinter import ttk
import time
import multiprocessing as mp

root = tk.Tk()
root.geometry('300x300+150+150')

# def sleep_func():
#     time.sleep(10)
#     lab['text'] = 'После сна'

# ==== multiprocessing
def check_process(p):
    if not p.is_alive():
        lab['text'] = 'Прошло 10 секунд\nЗадача выполнена в новом процессе\nПроцесс закрыт'
    root.after(1000, check_process, p)

def process():
    time.sleep(20)

def new_process():
    p = mp.Process(target=process)
    p.start()
    check_process(p)

# ==== Прежний код + изменения
# btn = ttk.Button(root, text='Run', command=sleep_func)  # Синхронное выполнение. Функция sleep_func запускается в том же потоке
btn = ttk.Button(root, text='Run', command=new_process)  # Мультипроцессорное выполнение. Функция new_process запускается в новом процессе
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text='Текст до нажатия')
lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)




if __name__ == '__main__':
    root.mainloop()
