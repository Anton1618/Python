'''Переопределение методов __iter__ и __next__, а также применение этого функционала в стороннем классе.

Протокол итератора, будучи определенным в классе итератора, позволяет ему в методе __iter__ возвращать самого себя
Для применения класса итератора в сторонних классах, он вызывается в методе __iter__ целевого класса, применяясь на всем
объекте или его определенном массиве, таким образом, возвращая свой экземпляр класса итератора.

Рассматриваются:
- class Letters - класс, в котором реализовано стандартное поведение итератора.
- class List - пустой класс, который наследуется от класса list.
- class InfIterator - реализация итератора, не ограниченного в количестве итераций.
- class UserIterator - реализация классического итератора.
- class Range - возвращает range-диапазон по элементам объекта.
- class RandomIterator - возвращает k-случайных чисел.
- class DoubleElementIterator - возвращает пары элементов объекта.
'''


class Letters:
    '''Класс, в котором реализовано стандартное поведение итератора'''
    def __init__(self, value):
        self.container = list(value)
    def __iter__(self):
        return iter(self.container)


class List(list):
    '''Пустой класс, который наследуется от класса list'''
    pass


class InfIterator:
    '''Реализация итератора, неограниченного в количестве итераций, за счет перевода индекса в начальное положение'''
    def __init__(self, value):
        self.value = value
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter


class InfIteratorIterable:
    '''Сторонний класс, реализующий пользовательский итератор InfIterator'''
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return InfIterator(self.value)


class UserIterator:
    '''Итератор, реализующий классическую работу итератора.
    Последовательно возвращает и удаляет элементы в массиве'''
    def __init__(self, value):
        self.container = list(value)
    def __iter__(self):
        return self
    def __next__(self):
        if not self.container:
            raise StopIteration
        item = self.container[0]
        del self.container[0]
        return f'<{item}>'


class UserIteratorIterable:
    '''Сторонний класс, реализующий пользовательский итератор UserIterator'''
    def __init__(self, value):
        self.container = list(value)
    def __iter__(self):
        return UserIterator(self.container)


class Range:
    '''Итератор, возвращающий range-диапазон по элементам объекта'''
    def __init__(self, start, stop, step):
        self.next = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.next > self.stop:
            raise StopIteration
        next_item = self.next
        self.next += self.step
        return next_item


class RangeIterable:
    '''Сторонний класс, реализующий пользовательский итератор Range'''
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return Range(self.start, self.stop, self.step)


class RandomIterator:
    '''Итератор, возвращающий k-случайных чисел'''
    from random import random
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.k:
            raise StopIteration
        self.i += 1
        return self.random()


def random_generator(k):
    '''Генераторная функция, выполняющая тот же принцип, что и пользовательский класс RandomIterator.
    Возвращает k-случайных чисел, но с более простой реализацией логики'''
    from random import random
    for _ in range(k):
        yield random()


class DoubleIterator:
    '''Итератор, возвращающий пары элементов объекта'''
    def __init__(self, value):
        self.container = list(value)
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i + 2 >= len(self.container):
            raise StopIteration
        self.i += 2
        return self.container[self.i-2], self.container[self.i-1]


class DoubleIteratorIterable:
    '''Сторонний класс, реализующий пользовательский итератор DoubleElementIterator'''
    def __init__(self, value):
        self.container = list(value)
    def __iter__(self):
        return DoubleIterator(self.container)


if __name__ == '__main__':
    print(' Классы с поведением для итерирования по умолчанию '.center(120, '-'))
    print(Letters.__doc__)
    letters_it = iter(Letters('qwerty'))
    for i in letters_it:
        print(i, end=' ')
    # q w e r t y
    print()
    print('Повторно')
    for i in letters_it:
        print(i, end=' ')
    # None
    print()

    print(List.__doc__)
    list_it = iter(List([1, 2, 3, 4, 5]))
    for pair in list_it:
        print(pair, end=' ')
    # 1 2 3 4 5
    print()
    print('Повторно')
    for i in list_it:
        print(i, end=' ')
    # None
    print()
    print()



    print(' InfIterator '.center(120, '-'))
    print(InfIterator.__doc__)
    inf_it = InfIterator('qwerty')
    for i in inf_it:
        print(i, end=' ')
    # q w e r t y
    print()
    print('Повторно')
    for i in inf_it:
        print(i, end=' ')
    # q w e r t y
    print()

    print(InfIteratorIterable.__doc__)
    infiteratoriterable_it = iter(InfIteratorIterable('qwerty'))
    for i in infiteratoriterable_it:
        print(i, end=' ')
    # q w e r t y
    print()
    print('Повторно')
    for i in infiteratoriterable_it:
        print(i, end=' ')
    # q w e r t y
    print()
    print()



    print(' UserIterator '.center(120, '-'))
    print(UserIterator.__doc__)
    useriterator_it = UserIterator('qwerty')
    for i in useriterator_it:
        print(i, end=' ')
    # <q> <w> <e> <r> <t> <y>
    print()
    print('Повторно')
    for i in useriterator_it:
        print(i, end=' ')
    # None
    print()

    print(UserIteratorIterable.__doc__)
    useriteratoriterable_it = iter(UserIteratorIterable('qwerty'))
    for i in useriteratoriterable_it:
        print(i, end=' ')
    # <q> <w> <e> <r> <t> <y>
    print()
    print('Повторно')
    for i in useriteratoriterable_it:
        print(i, end=' ')
    # None
    print()
    print()



    print(' Range '.center(120, '-'))
    print(Range.__doc__)
    range_it = Range(1, 10, 2)
    for num in range_it:
        print(num, end=' ')
    # 1 3 5 7 9
    print()
    print()

    print(RangeIterable.__doc__)
    for num in RangeIterable(1, 10, 2):
        print(num, end=' ')
    # 1 3 5 7 9
    print()
    print()



    print(' RandomIterator '.center(120, '-'))
    print(RandomIterator.__doc__)
    for x in RandomIterator(3):
        print(x)
    # 0.6454400647167301
    # 0.6232398624624254
    # 0.5607588517964365
    print()

    print(random_generator.__doc__)
    gen = random_generator(3)
    for i in gen:
        print(i)
    # 0.4831366133543832
    # 0.8193533862899688
    # 0.7374135444753213
    print()
    print()



    print(' DoubleElementIterator '.center(120, '-'))
    print(DoubleIterator.__doc__)
    for pair in DoubleIterator([1, 2, 3, 4, 5]):
        print(pair, end=' ')
    # (1, 2) (3, 4)
    print()
    print()

    print(DoubleIteratorIterable.__doc__)
    for pair in DoubleIteratorIterable([1, 2, 3, 4, 5]):
        print(pair, end=' ')
    # (1, 2) (3, 4)
    print()
    print()



