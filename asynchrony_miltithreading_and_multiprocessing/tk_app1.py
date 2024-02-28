'''
# Функционал
Окно приложения с возможностью нажатия на кнопку и запуска работы.
Моделирование работы приложения представлено инструкцией time.sleep(10) и сопровождается сменой текста в окне.


## Цель демонстрации
Отразить факт упорядоченного выполнения задач в синхронном коде, когда при запуске событийного цикла, по умолчанию, нельзя исполнять несколько задач одновременно
Так например, нельзя одновременно обновлять состояние окна приложения и выполнять некий функционал, потому что при запуске функционала, это приведет к зависанию окна и отсутствию реагирования на действия пользователя

Процесс
1. При запуске GUI окна, будет создан новый процесс для функционирования программы - новый процесс python в диспетчере задач.
2. Пока программа не активна и не выполняется её функционал (time.sleep(10)), цикл событий mainloop, запущенный для обслуживания этого окна, позволяет перемещать окно приложения и взаимодействовать с элементами на нём.
3. Когда, посредством нажатия на кнопку в приложении, запускается функционал (time.sleep(10)), взаимодействие с окном прекращается, оно "замерает" и не отвечает на действия.
Пока функционал не будет выполнен, дальнейшие действия с окном невозможны, цикл событий приложения mainloop не отвечает
4. Когда функционал будет выполнен, вернется возможность взаимодействовать с окном приложения


## Решение проблемы выбирается исходя из типа задачи
• Мультипроцессинг - Требование процессорного времени
Применяется для решения высоконагруженных задач, например, рендер видео из картинок, когда вся нагрузка ложиться на процессор
Применение мультипроцессинга: tk_app1_with_multiprocessing.py

• Многопоточность - Большое количество параллельных I/O операций (ввода-вывода)
Применяется для решения легких задач, например, запрос к базе данных, обращение к API сервера и тп.
Применение многопоточности: tk_app1_with_threading.py

• Асинхронность - Большое количество параллельных I/O операций (ввода-вывода)
Хорошо подходит для сетевого программирования, масштабируемых веб-серверов, систем с большим количеством параллельных I/O операций.
Применение асинхронности: tk_app1_with_asynchrony.py
'''

import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.geometry('300x300+150+150')

def sleep_func():
    time.sleep(10)  # Моделирование работы приложения
    lab['text'] = 'После сна'

btn = ttk.Button(root, text='Run', command=sleep_func)  # Синхронное выполнение. Функция sleep_func запускается в том же потоке
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text='Текст до нажатия')
lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)




if __name__ == '__main__':
    root.mainloop()
