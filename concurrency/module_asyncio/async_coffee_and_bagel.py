'''
Асинхронное выполнение функций с замером времени
'''

import time
import asyncio

async def brewCoffee():
    print('Start brewCoffee()')
    await asyncio.sleep(3)
    print('End breCoffee()')
    return 'Coffee ready'

async def toastBagel():
    print('Start toastBagel()')
    await asyncio.sleep(2)
    print('End toastBagel()')
    return 'Bagel toasted'


async def main():
    '''Пользовательская функция событийного цикла event loop для координирования асинхронных функций'''
    start_time = time.time()

    # Раздельный способ задействия сопрограмм
    # coffee_task = asyncio.create_task(brewCoffee())  # Предподготовка корутины, созданием задачи
    # toast_task = asyncio.create_task(toastBagel())  # Предподготовка корутины, созданием задачи

    # Выполнение задачи через оператор await в библиотеке asyncio, на подобии yield в генераторах, сигнализируя, если задача не выполняется, то может быть приостановлена, для выполнения других задач
    # result_coffee = await coffee_task  # Или просто await coffee_task для выполнения задачи
    # result_bagel = await toast_task  # Или просто await toast_task для выполнения задачи


    # Совместный способ задействия сопрограмм
    batch = asyncio.gather(brewCoffee(), toastBagel())  # Совместная предподготовка корутин для параллельного выполнения. Возвращаемые значения будут получены в том же порядке, в котором были переданы аргументы корутин
    result_coffee, result_bagel = await batch  # Совместное выполнение задач

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'Result of brewCoffee: {result_coffee}')
    print(f'Result of toastBagel: {result_bagel}')
    print(f'Total execution time: {elapsed_time:.2f} seconds')




if __name__ == '__main__':
    asyncio.run(main())
