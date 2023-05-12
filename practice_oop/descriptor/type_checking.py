'''Проверка типов дескриптором TypeCheck, который проверяет типы атрибутов x и y класса MyClass.
Если тип значения не соответствует ожидаемому типу, возбуждается исключение TypeError.'''


class TypeCheck:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"value must be of type {self.expected_type.__name__}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:
    x = TypeCheck(int)
    y = TypeCheck(str)

    def __init__(self, x, y):
        self.x = x
        self.y = y