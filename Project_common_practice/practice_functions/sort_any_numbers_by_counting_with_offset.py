from random import randint
def number_count(lst):
    '''Сортировка подсчетом со смещением для неограниченного диапазона чисел'''
    offset_number_count_lst = [0] * len(range(min(lst)-1, max(lst)))
    index_offset = abs(difference) if (difference:=min(lst))<0 else -difference
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
    assert number_count([8, 5, 5, 10, 8, 7])  == [(5, 2), (7, 1), (8, 2), (10, 1)]
    assert number_count([-9, -9, -4, -4, -10, -2,]) == [(-10, 1), (-9, 2), (-4, 2), (-2, 1)]
    print(number_count([randint(1000, 1010) for i in range(50)]))
    print(number_count([randint(-1010, -1000) for i in range(50)]))
