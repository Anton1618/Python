'''Дескриптор Cached кэширует результат вычисления метода calculate_sum класса MyClass.
Результат вычисления запоминается в словаре cache до тех пор, пока значения атрибутов x и y не изменятся.'''


class Cached:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance not in self.cache:
            self.cache[instance] = self.func(instance)
        return self.cache[instance]


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @Cached
    def calculate_sum(self):
        return self.x + self.y