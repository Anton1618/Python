'''Определение пользовательской функции next() - Iterator и простого итерируемого объекта - Letters

Iterator - Реализация функционала next, эквивалентно поведению обычной функции next
Letters - Реализация итерируемого объекта, для этого достаточно возвращать объект от Iterator или встроенной iter
'''


class Iterator:
    def __init__(self, value):
        self.container = []
        for i in value:
            self.container.append(f'-{i}-')
    def __next__(self):
        if self.container == []:
            raise StopIteration
        item = self.container[0]
        del self.container[0]
        return item
    def __iter__(self):
        return self
# Прямая передача в итератор
for i in Iterator([1, 2, 3, 4, 5]):
    print(i, end=' ')
'-1- -2- -3- -4- -5-'


class Letters:
    def __init__(self, value):
        self.container = []
        for i in value:
            self.container.append(f'-{i}-')
    # Может либо применяться встроенный итератор
    # def __iter__(self):
    #     return iter(self.container)
    # Либо может применяться пользовательский итератор
    def __iter__(self):
        return Iterator(self.container)

# На примере задействия пользовательского итератора
for i in iter(Letters('qwerty')):
    print(i, end=' ')
'--q-- --w-- --e-- --r-- --t-- --y--'