'''Декораторы'''


# === Декораторы HTMl тегов ===
def header(func):
    def inner(*args, **kwargs):
        return '<h1>' + '\n' + str(func(*args, **kwargs)) + '\n' + '</h1>'

    return inner


def table(func):
    def inner(*args, **kwargs):
        return '<table>' + '\n' + str(func(*args, **kwargs)) + '\n' + '</table>'

    return inner


# --- Функция вывода строки для декорирования ---
@table
@header
def hello(name, surname):
    return f"Hello, {name} {surname}"


# === Декоратор счетчик обращений к функции ===
def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__}, вызывалась {count} раз', sep='\n')
        return func(*args, **kwargs)

    return inner


# --- Функции математических операций для декорирования ---
@counter
def mult(a, b, c):
    return a * b * c


@counter
def add(a, b):
    return a + b


# === Декоратор скорости выполнения функции ===
def benchmark(function):
    from time import time
    def inner(*args, **kwargs):
        st = time()
        result = function(*args, **kwargs)
        et = time()
        print(f'Время выполнения функции {function.__name__}: {round(et - st, 2)} секунд')
        return result

    return inner


# --- Функции нахождения НОД для декорирования ---
@benchmark
def slow_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@benchmark
def fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


# --- Функция получения response ответа от сервера для декорирования ---
@benchmark
def fetch_webpage(url):
    import requests
    return requests.get(url)


# === Декоратор генераторной функции ===
def gen_decorator(func):
    def inner(*args, **kwargs):
        print(' --- Start decorator --- ')
        gen_res = func(*args, **kwargs)
        print([round(i, 4) for i in gen_res])
        return ' --- Finish decorator --- '

    return inner


# --- Функции нахождения НОД для декорирования ---
@gen_decorator
def random_generator(k):
    from random import random
    for i in range(k):
        yield random()


if __name__ == '__main__':
    print('Декораторы html тегов'.center(80, '-'))
    print(hello('Anton', 'kramskiy'))
    print()

    print('Декоратор счетчик обращений к функции'.center(80, '-'))
    print([mult(2, 10, 1) for i in range(3)])
    print()
    print([add(10, 5) for i in range(3)])
    print()

    print('Декоратор скорости выполнения функции'.center(80, '-'))
    print(slow_nod(10_000_000, 2))
    print()
    print(fast_nod(10_000_000, 2))
    print()

    print('Декоратор скорости выполнения функции'.center(80, '-'))
    print(fetch_webpage('https://Google.com'))
    print()

    print('Декоратор генераторной функции'.center(80, '-'))
    print(random_generator(5))
