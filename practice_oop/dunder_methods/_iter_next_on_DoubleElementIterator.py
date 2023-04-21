'''Пользовательский итератор для парного кортежного возвращения элементов.

Счетчик-индекс осуществляет приращение, при котором на каждой итерации становятся доступны два элемента массива,
последний и предпоследний.
Если проверка на получение двух значений не выполняется, то итерация прекращается
Таким образом, полностью реализуется только четный диапазон значений, для нечетного не сможет быть возвращен последний
элемент
'''


class DoubleElementIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i+2 >= len(self.lst):
            raise StopIteration
        self.i += 2
        return self.lst[self.i-2], self.lst[self.i-1]


class MyListDouble(list):
    '''Выполняет итерирование на основе вы'''
    def __iter__(self):
        return DoubleElementIterator(self)


class MyListDefault(list):
    '''Осуществляет стандартное итерирование'''
    pass


if __name__ == '__main__':
    print('Получение пар значений через класс DoubleElementIterator')
    for pair in DoubleElementIterator([1, 2, 3, 4, 5]):
        print(pair, end=' ')
    print()

    print('Получение пар значений через сторонний класс, реализующий пользовательский double-итератор')
    for pair in MyListDouble([1, 2, 3, 4, 5]):
        print(pair, end=' ')
    print()

    print('Получение значений через сторонний класс, применяющий стандартный итератор элементов')
    for pair in MyListDefault([1, 2, 3, 4, 5]):
        print(pair, end=' ')
    print()
