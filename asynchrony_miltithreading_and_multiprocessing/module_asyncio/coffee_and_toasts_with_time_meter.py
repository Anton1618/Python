'''Асинхронное выполнение функций с замером времени'''

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
    '''Базовая область запука и приостановки сопрограммам'''
    start_time = time.time()

    batch = asyncio.gather(brewCoffee(), toastBagel())
    # Возвращаемые значения будут получены в том же порядке, в котором были переданы аргументы сопрограмм
    result_coffee, result_bagel = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'Result of brewCoffee: {result_coffee}')
    print(f'Result of toastBagel: {result_bagel}')
    print(f'Total execution time: {elapsed_time:.2f} seconds')




if __name__ == '__main__':
    asyncio.run(main())
