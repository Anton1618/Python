from random import randint
def number_count(lst):
    '''Сортировка подсчетом со смещением для диапазона чисел с
    обязательным наличием отрицательной величины'''
    offset_number_count_lst = [0] * len(range(min(lst)-1, max(lst)))
    index_offset = abs(min(lst))
    for i in lst:
        offset_number_count_lst[i+index_offset] += 1
    result = []
    for i in range(len(offset_number_count_lst)):
        if offset_number_count_lst[i] > 0:
            result.append((i-index_offset, offset_number_count_lst[i]))
    return result


if __name__ == '__main__':
    assert number_count([8, -8, -2, -4, 9, -9]) == [(-9, 1), (-8, 1), (-4, 1), (-2, 1), (8, 1), (9, 1)]
    assert number_count([-1, 1, 1, -1, 1, 0, 1, 1, -1, -1]) == [(-1, 4), (0, 1), (1, 5)]
    assert number_count([-9, -9, -4, -4, -10, -2,]) == [(-10, 1), (-9, 2), (-4, 2), (-2, 1)]
