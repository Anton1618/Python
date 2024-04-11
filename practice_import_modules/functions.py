'''Различные полезные функции'''

print(f'Import module functions{__name__}')

def find_module(*args):
    """Вывод результата поиска модуля"""
    import sys
    for i in sys.builtin_module_names:
        if i in args:
            print(f" --- Найден модуль {i}! --- ")


# find = find_module('sys', 'math')
# print(find)



