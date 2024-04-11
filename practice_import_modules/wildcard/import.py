from practice_functions.staff_functions import pretty_header as __pretty_header
# import sys


# class DebugFinder:
#     '''Неизвестный функционал'''
#     @classmethod
#     def find_spec(cls, name, path, target=None):
#         print(f"Importing {name!r}")
#         return None
# sys.meta_path.insert(0, DebugFinder)


def vars_check():
    '''Отображение всех пользовательских переменных в модуле на текущий момент'''
    print('Скачанные переменные:')
    vars = list(globals().keys())
    for var in vars:
        if ('__' not in var) and (var not in ('vars_check', 'vars', 'var')):
            if '__package__' in dir(module:=globals()[var]):
                varval_dct = {var_val:getattr(module, var_val) for var_val in dir(module) if '__' not in var_val}
                print(f'{module.__name__} - модуль, его переменные:', varval_dct)
            else:
                print(var)
            del globals()[var]
    print()




if __name__ == '__main__':
    __pretty_header('Импортирование переменных из модуля data.py, которые перечислены в переменной __all__ этого модуля')
    print('Размещение идентификаторов переменных в переменной __all__, позволяет получить эти переменные, в процессе импорта всех объектов данного модуля')
    from data import *
    vars_check()


    __pretty_header('Импортирование переменных из пакета src, которые перечисленны в переменной __all__ модуля __init__')
    print('Размещение идентификаторов переменных в переменной __all__, позволяет получить эти переменные, в процессе импорта всех объектов данного пакета, аналогично модулю')
    from src import *
    vars_check()


    __pretty_header('Импортирование переменных и модулей из пакета lib, которые перечислены в переменной __all__ модуля __init__')
    print('Если в файле __init__ размещаются идентификаторы модулей текущего пакета, то они также будут импортированы, при импортре всех объектов пакета') 
    from lib import *
    vars_check()