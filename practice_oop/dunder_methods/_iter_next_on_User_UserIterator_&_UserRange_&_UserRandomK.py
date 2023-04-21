'''Реализация пользовательских итераторов, а также их применение в стороннем классе для итерирования его элементов.

Рассматриваются:
- class Iterator - реализация принципа итерирования итератора
- class Range - реализация функции range()
- class RandomIterator - возвращает k-случайных чисел
'''


class Iterator:
    '''Пользовательский итератор, реализующий процесс получения элементов из итератора.
    Последовательно возвращает и удаляет элементы в массиве'''
    def __init__(self, value):
        self.container = []
        for i in value:
            self.container.append(f'-{i}-')
    def __iter__(self):
        return self
    def __next__(self):
        '''В отличие от стандартного итерирования, метод не применяет счетчик, а всегда обращается к текущему элементу
        В процессе итерирования он возвращает и удаляет этот элемент.
        Останавливается, когда атрибут объекта становится пуст'''
        if self.container == []:
            raise StopIteration
        item = self.container[0]
        del self.container[0]
        return item


class LettersStandart:
    '''Сторонний класс, реализующий стандартное итерирование элементов'''
    def __init__(self, value):
        self.container = []
        for i in value:
            self.container.append(f'-{i}-')
    def __iter__(self):
         return iter(self.container)


class LettersUserIterator:
    '''Сторонний класс, реализующий пользовательский итератор'''
    def __init__(self, value):
        self.container = []
        for i in value:
            self.container.append(f'-{i}-')
    def __iter__(self):
        return Iterator(self.container)


class Range:
    '''Пользовательский итератор, возвращающий range-диапазон'''
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
    '''Сторонний класс, реализующий пользовательский итератор range-диапазона'''
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return Range(self.start, self.stop, self.step)


class RandomIterator:
    '''Пользовательский итератор, возвращающий k-случайных чисел'''
    from random import random
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i > self.k:
            raise StopIteration
        self.i += 1
        return self.random()


def random_generator(k):
    '''Генераторная функция, выполняющая тот же принцип, что и пользовательский класс,
    возвращающий k-случайных чисел, но с более простой реализацией логики'''
    from random import random
    for i in range(k):
        yield random()


if __name__ == '__main__':
    print(' Реализация принципа обработки итератора '.center(120, '-'))
    print('Применение для итерирования пользовательского класса iterator')
    for i in Iterator('qwerty'):
        print(i, end=' ')
    print()
    for i in Iterator([1, 2, 3]):
        print(i, end=' ')
    # -q- -w- -e- -r- -t- -y-
    # -1- -2- -3-
    print()

    print('Применение для итерирования стандартной функции iter()')
    for i in iter(LettersStandart('qwerty')):
        print(i, end=' ')
    print()
    for i in iter(LettersStandart([1, 2, 3])):
        print(i, end=' ')
    # -q- -w- -e- -r- -t- -y-
    # -1- -2- -3-
    print()

    print('Применение пользовательского итератора в стороннем классе')
    for i in iter(LettersUserIterator('qwerty')):
        print(i, end=' ')
    print()
    for i in iter(LettersUserIterator([1, 2, 3])):
        print(i, end=' ')
    # --q-- --w-- --e-- --r-- --t-- --y--
    # --1-- --2-- --3--
    print()
    print()


    print(' Применение пользовательского итератора, возвращающего range-диапазон по элементам массива '.center(120, '-'))
    print('Получение range-диапазона от пользовательского класса Range')
    for num in Range(1, 10, 2):
        print(num, end=' ')
    # 1 3 5 7 9
    print()

    print('Получение range-диапазона от пользовательского метода в стороннем классе')
    for num in RangeIterable(1, 10, 2):
        print(num, end=' ')
    # 1 3 5 7 9
    print()
    print()


    print(' Применение пользовательского итератора и функции, для возвращения k-случайных чисел '.center(120, '-'))
    print('Получение k-случайных чисел от пользовательского класса RandomIterator')
    for x in RandomIterator(3):
        print(x)
    # 0.6454400647167301
    # 0.6232398624624254
    # 0.5607588517964365
    # 0.59106925883583

    print('Получение k-случайных чисел от генераторной функции random_generator')
    gen = random_generator(3)
    for i in gen:
        print(i)
    # 0.4831366133543832
    # 0.8193533862899688
    # 0.7374135444753213
    print()
    print()


