'''
Чем асинхронность лучше многопоточности?

Многопоточность подвержена потоковой НЕ безопасности trashing - снижению эффективности многопоточности, ввиду чрезмерно большого объема времени, при переключении контекста между потоками

Асинхронность, напротив, выполняется в рамках одного потока, благодаря чему отсутствует необходимость в переключении между потоками


Все вызовы функции simplePrint планируются и выполняются вместе в цикле событий event loop (функции main), в соответствии с заданным параметром переменной цикла. А каждый следующий вызов функции получает аргумент счетчика цикла, для применения в своих инструкциях, в частности, для выдерживания задержки своего выполнения 
'''

import asyncio
import time

def simplePrint(sec):
    start_time = time.time()
    time.sleep(sec)
    end_time = time.time()
    print(f'Задача выполнена за {end_time - start_time} секунд')

async def acyncPrint(sec):
    start_time = time.time()
    await asyncio.sleep(sec)
    end_time = time.time()
    print(f'Задача выполнена за {end_time - start_time} секунд')


def simpleMain():
    for time_await in range(1, 16):
        simplePrint(time_await)

async def asyncMain():
    async with asyncio.TaskGroup() as tg:
        for time_await in range(1, 16):
            tg.create_task(acyncPrint(time_await))


if __name__ == '__main__':
    start = time.time()

    simpleMain()
    # asyncio.run(asyncMain())

    print(f'Время выполнения: {time.time() - start}')
