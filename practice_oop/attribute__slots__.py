'''Сравнение __slots__ и __dict__'''

from pympler.asizeof import asizeof
from sys import getsizeof

class PersonA:
    __slots__ = ['name', 'surname']
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class PersonB:
    __slots__ = ['name', 'surname', '__dict__']
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class PersonC:
    FIELDS = ['name', 'surname']
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

if __name__ == '__main__':
    print('Сравнение методов подсчета веса:')
    dct1 = {"key": "value"}
    dct2 = {"key": {"key2": "value"}}
    print('Функцией sys.getsizeof')
    print(getsizeof(dct1))
    print(getsizeof(dct2))
    print('Функцией pympler.asizeof')
    print(asizeof(dct1))
    print(asizeof(dct2))
    print()

    a1 = PersonA('artem', 'potapov')
    b1 = PersonB('nikita', 'barencev')
    c1 = PersonC('anastasia', 'afdeeva')

    print('Размер объектов getsizeof:')
    print(getsizeof(a1))
    print(getsizeof(b1))
    print(getsizeof(c1))
    print()

    print('Размер объектов asizeof')
    print(asizeof(a1))
    print(asizeof(b1))
    print(asizeof(c1))




