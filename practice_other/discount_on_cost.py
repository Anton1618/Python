'''Функция вычисляет цену с учетом налога и скидки.

Представлены две функции, которые могут принимать аргументы, рассчитывать на их основе результат и возвращать его:
- Функция принимает аргументы переменной длины.
- Функция принимает аргументы фиксированной длины.
'''


def result_price(price=None, max_discount=0.50, **kwargs):
    '''Функция принимает аргументы переменной длины.
    Аргументами могут стать возможно переданное значение скидки и налога'''
    if not price:
        raise ValueError('Должно быть обязательно передано значение стоимости')
    tax = kwargs.get('tax')
    discount = kwargs.get('discount')
    if tax:
        price = price * (1 + tax)
    if discount:
        discounted_price = price * (1 - discount)
        if discounted_price >= price * (1 - max_discount):
            price = discounted_price
        else:
            raise ValueError(f'Скидка не может быть более {max_discount:.0%}')
    return round(price, 2)


def result_price2(price=None, max_discount=0.50, tax=0.18, discount=0.15):
    '''Функция принимает аргументы фиксированной длины.
    Могут быть переданы значения скидки или налога, либо применены значения по умолчанию'''
    if not price:
        raise ValueError('Должно быть обязательно передано значение стоимости')
    price = price * (1 + tax)
    discounted_price = price * (1 - discount)
    if discounted_price >= price * (1 - max_discount):
        price = discounted_price
    else:
        raise ValueError(f'Скидка не может быть более {max_discount:.0%}')
    return round(price, 2)


if __name__ == '__main__':
    print('Функция с параметрами переменной длины')
    # print(result_price())  # ValueError: Должно быть обязательно передано значение стоимости
    assert result_price(1500) == 1500
    assert result_price(1500, discount=0, tax=0) == 1500
    assert result_price(1500, discount=0.50) == 750.0
    # print(result_price(1500, discount=0.51))  # ValueError: Скидка не может быть более 50%
    assert result_price(1500, discount=0.50, tax=0) == 750.0
    # print(result_price(1500, discount=0.51, tax=0))  # ValueError: Скидка не может быть более 50%
    assert result_price(1500, discount=0.0000001, tax=0) == 1500.0
    assert result_price(1500, discount=0.50, tax=1) == 1500.0
    assert result_price(1500, discount=0.50, tax=2) == 2250.0
    assert result_price(1500, discount=0.50, tax=0.00001) == 750.01


    print('Функция с параметрами по умолчанию')
    # print(result_price2())  # ValueError: Должно быть обязательно передано значение стоимости
    assert result_price2(1500) == 1504.5
    assert result_price2(1500, discount=0, tax=0) == 1500
    assert result_price2(1500, discount=0.50) == 885.0
    # print(result_price(1500, discount=0.51))  # ValueError: Скидка не может быть более 50%
    assert result_price2(1500, discount=0.50, tax=0) == 750.0
    # print(result_price(1500, discount=0.51, tax=0))  # ValueError: Скидка не может быть более 50%
    assert result_price2(1500, discount=0.0000001, tax=0) == 1500.0
    assert result_price2(1500, discount=0.50, tax=1) == 1500.0
    assert result_price2(1500, discount=0.50, tax=2) == 2250.0
    assert result_price2(1500, discount=0.50, tax=0.00001) == 750.01
    print('Все тесты пройдены')
