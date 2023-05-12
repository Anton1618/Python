'''Ленивая инициализация дескриптором LazyInit, который позволяет лениво инициализировать атрибут calculate_sum
класса MyClass.
Значение атрибута вычисляется при первом доступе к нему и запоминается в словаре __dict__'''


class LazyInit:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        instance.__dict__[self.name] = value
        return value

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @LazyInit
    def calculate_sum(self):
        return self.x + self.y