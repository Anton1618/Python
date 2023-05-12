'''Дескриптор MaxValue ограничивает значения атрибутов x и y класса MyClass от 0 до 10 и до 100 соответственно
'''


class MaxValue:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __set__(self, instance, value):
        if not self.min_val < value < self.max_val:
            raise ValueError(f'Значение {value} должно быть в диапазоне от {self.min_val} до {self.max_val}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:
    x = MaxValue(0, 10)
    y = MaxValue(0, 100)

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    m1 = MyClass(5, 80)
    # m2 = MyClass(-1, 150)  # ValueError: Значение -1 должно быть в диапазоне от 0 до 10