'''
# Асинхронные функции
Вместо обычных функций и методов используются асинхронные функции и методы, которые для отложенного выполнения операций ввода/вывода возвращают asyncio "futures" или "tasks". Они объявляются с использованием ключевого слова async

# Awaitables
Асинхронные функции обычно содержат одно или несколько выражений await для асинхронных вызовов, что позволяет функции "ожидать" завершения операции без блокировки событийного цикла. Когда такая функция достигает await, она возвращает управление циклу событий, позволяя другим задачам продолжить выполнение

# Event Loop
Запуск асинхронных функций осуществляется из цикла событий event loop (пользовательская функция), который координирует выполнение асинхронных операций и вызовы колбэков
'''

import asyncio
import time

def simplePrint1():
    print('Выполнен print #1')

def simplePrint2():
    time.sleep(4)
    print('Выполнен print #2')

def simplePrint3():
    time.sleep(2)
    print('Выполнен print #3')


async def asyncPrint1():
    print('Выполнен print #1')

async def asyncPrint2():
    await asyncio.sleep(4)
    print('Выполнен print #2')

async def asyncPrint3():
    await asyncio.sleep(2)
    print('Выполнен print #3')


def simpleMain():
    simplePrint1()
    simplePrint2()
    simplePrint3()

async def asyncMain():
    # Вариант раздельной предподготовки сопрограмм и их запуск
    # task1 = asyncio.create_task(asyncPrint1())  # Предподготовка корутины, созданием задачи
    # task2 = asyncio.create_task(asyncPrint2())  # Предподготовка корутины, созданием задачи
    # task3 = asyncio.create_task(asyncPrint3())  # Предподготовка корутины, созданием задачи

    # Выполнение задачи через оператор await в библиотеке asyncio, на подобии yield в генераторах, сигнализируя, что если задача не выполняется, то может быть приостановлена, для выполнения других задач
    # await task1
    # await task2
    # await task3


    # Вариант совместной предподготовки сопрограмм и их запуск
    # -- Совместная предподготовка корутин для параллельного выполнения. Возвращаемые значения будут получены в том же порядке, в котором были переданы аргументы корутин
    # tasks = asyncio.gather(asyncPrint1(), asyncPrint2(), asyncPrint3())
    # await tasks  # Совместное выполнение задач

    # -- Простое выполнение корутин напрямую через оператор await
    # await asyncio.gather(asyncPrint1(), asyncPrint2(), asyncPrint3())

    # -- Раздельная предподготовка корутин, например через формирование списка задач в цикле, с его дальнейшей распаковкой для выполнения методом gather через оператор await
    # tasks = []
    # for task in (asyncPrint1, asyncPrint2, asyncPrint3):
    #     tasks.append(asyncio.create_task(task()))
    # await asyncio.gather(*tasks)

    # -- Метод предподготовки корутин через файловый объект TaskGroup, как аналогичной точки входа каждой отдельной фукнции
    async with asyncio.TaskGroup() as tg:
        tg.create_task(asyncPrint1())
        tg.create_task(asyncPrint2())
        tg.create_task(asyncPrint3())




if __name__ == '__main__':
    # simpleMain()  # Синхронное последовательное выполнение
    asyncio.run(asyncMain())  # Асинхронное одновременное выполнение
