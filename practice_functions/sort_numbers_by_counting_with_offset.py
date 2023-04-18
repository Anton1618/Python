'''Сортировка со смещением для числовых данных. Осуществляется относительно их значения
Процесс аналогичен, за исключением необходимости применения поиска и определения кодовых точек Unicode
Построение сохраняющего массива основано на вычислении: сохраняющий массив = [0] * (max(объект) - min(объект) + 1)
Или длине сформированного диапазона на этих значениях: сохраняющий массив = [0] * len(range(min(lst), max(lst)+1))
'''
from random import randint


def number_count(lst):
    '''Подсчет и сортировка со смещением только числовых значений'''
    offset = min(lst)
    lst_count = [0] * (max(lst) - min(lst) + 1)
    index_offset = abs(offset) if offset < 0 else -offset
    for i in lst:
        lst_count[i + index_offset] += 1
    result = []
    for i in range(len(lst_count)):
        if lst_count[i] > 0:
            result.append((i-index_offset, lst_count[i]))
    return result


if __name__ == '__main__':
    assert number_count([8, -8, -2, -4, 9, -9]) == [(-9, 1), (-8, 1), (-4, 1), (-2, 1), (8, 1), (9, 1)]
    assert number_count([-1, 1, 1, -1, 1, 0, 1, 1, -1, -1]) == [(-1, 4), (0, 1), (1, 5)]
    assert number_count([8, 5, 5, 10, 8, 7]) == [(5, 2), (7, 1), (8, 2), (10, 1)]
    assert number_count([-9, -9, -4, -4, -10, -2]) == [(-10, 1), (-9, 2), (-4, 2), (-2, 1)]
    print('Все тесты пройдены')
