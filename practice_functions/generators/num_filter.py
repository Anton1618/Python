'''
# Посимвольная фильтрация элементов коллекции, для получения всех цифр


## Input
Принимает коллекцию элементов: `list`, `tuple`, `dict`, `str`, `set`
и возвращает исключение TypeError, в противном случае

Обрабатывает элементы, которые соответствуют типу: `str`, `int`, `float`, `bool`


## Output
Возвращает итератор с найденной цифрой, преобразованной в целое число: `int(elm)`
'''

def num_filter(collection) -> iter:
    if type(collection) not in (list, tuple, dict, str, set):
        raise TypeError('Аргументом функции может быть только итерируемая коллекция')

    was_er = False
    for elm in collection:
        if type(elm) in (str, int, float, bool):
            try:
                yield int(elm)
            except ValueError:
                if was_er == False:
                    print('Присутствуют элементы, которые нельзя преобразовать!')
                was_er = True




if __name__ == '__main__':
    assert [i for i in num_filter([1, 2, 3])] == [1, 2, 3]
    assert [i for i in num_filter(['1', 2, '3'])] == [1, 2, 3]
    assert {i for i in num_filter({'1', 2, '3'})} == {1, 2, 3}
    assert [i for i in num_filter({'1': None, 2: None, '3': None})] == [1, 2, 3]
    assert [i for i in num_filter('he11o, wor1d 42!')] == [1, 1, 1, 4, 2]  # Присутствуют элементы, которые нельзя преобразовать


    print('\n\n✅ Все тесты пройдены')
