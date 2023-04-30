'''Класс, с определенным методом __call__, который позволяет применять объект класса для декорирования.

Реализация таймера
Аналогично декоратору в функциональном программировании, принимает функцию и оборачивает её заданным функционалом
Функция сохраняется как атрибут объекта-декоратора
Важной особенностью реализации является декорирование функции с рекурсией, для которой должна быть сохранена ссылка на
первоначальную функцию.
Потому как, если в объекте реализован принцип вызова, сохранение в нем ссылки на функцию, приведет к множественному
вызову этого объекта во время рекурсии
'''
from time import perf_counter


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызов функции {self.func.__name__}')
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция выполнена за {finish - start}')
        return result


def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= 1
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print('Факториал числа')
    decor_fact = Timer(fact)
    print(decor_fact(35))
    print()

    print('Число Фибоначчи')
    decor_fib = Timer(fib)
    print(decor_fib(35))
