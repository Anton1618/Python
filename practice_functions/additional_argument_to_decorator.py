'''Построение декоратора с возможностью передачи аргументов

Рассматривается декорирование производной функции
'''
import math


def decorator(func):
    '''Декоратор производной функции'''
    def inner(x, *args, **kwargs):
        dx = 0.01
        res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
        return res
    return inner


def df_decorator(dx=0.01):
    '''Декоратор производной функции, с возможностью передачи аргумента точности'''
    def decorator(func):
        def inner(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        return inner
    return decorator


def sin_df(x):
    return math.sin(x)


decor = decorator(sin_df)
df_decor = df_decorator(0.0000001)(sin_df)


if __name__ == '__main__':
    print(sin_df(math.pi/3))
    print(decor(math.pi/3))
    print(df_decor(math.pi/3))
