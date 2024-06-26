'''
Проверка путей, на возможность импорта или вызова модулей из них
'''

def check_path_from_syspath(*target_paths) -> list[bool]:
    '''# Проверка путей, на возможность импорта или вызова модулей из них
    
    Функция проверяет директории, пути которых присутствуют в sys.path. Модули и другие директории, которые доступны при проверке считаются доступными для вызова и импортирования 

    Целевые пути для проверки добавляются ключами в словарь, где, изначально, значениями для этих ключей устанавливается False.
    При истинности проверки, значение False будет изменено на значение True
    

    ### Параметры:
    `target_paths`: одна или множество строк путей, например "C:\\Users\\your_name\\Desctop\\project42" или "/home/user/project42", "/home/user/project69"


    ### Возвращаемое значение:
    `[bool]`: список одного или множества булевых значений, соответствующих аргументам, в том порядке, в котором они были переданы


    ### Примеры:
    ```python
    check_path_from_syspath()  # []
    check_path_from_syspath('C:\\Projects\\app42')  # [True]
    check_path_from_syspath('C:\\abracadabra')  # [False]
    check_path_from_syspath('C:\\Projects\\app42', 'C:\\abracadabra')  # [True, False]
    ```
    '''
    from sys import path as syspath
    from os import listdir
    
    target_dct = {path:False for path in target_paths}

    for next_sys_p in syspath:
        for target_p in target_paths:
            available_paths_lst = []
            try:
                available_paths_lst = listdir(next_sys_p)
            except (NotADirectoryError, FileNotFoundError):
                pass
            if [True for next_p in available_paths_lst if next_p in target_p]:
                target_dct[target_p] = True

    for st, val in target_dct.items():
        print(f'{val!r:<6}: {st}')
    
    return list(target_dct.values())



if __name__ == '__main__':
    print('===========================================================================')
    print('Примеры директорий sys.path')
    syspath_example = ['C:\\Python312\\Scripts\\ipython.exe',
                        'C:\\GoogleDrive\\Python',
                        'C:\\Python312\\python312.zip',
                        'C:\\Python312\\DLLs',
                        'C:\\Python312\\Lib',
                        'C:\\Python312',
                        '',
                        'C:\\Python312\\Lib\\site-packages']
    print(*syspath_example, sep='\n')


    print('===========================================================================')
    print('Примеры директорий для проверки')
    target_paths = ('C:\\GoogleDrive\\Python\\module_json',
                    'C:\\GoogleDrive\\Python\\practice_import_modules\\myapp', 
                    'C:\\abracadabra', 
                    'C:\\GoogleDrive\\abracadabra')
    print(*target_paths, sep='\n')


    print('===========================================================================')
    print('Проверка с передачей множества аргументов')
    assert check_path_from_syspath(*target_paths) == [True, True, False, False]


    print('===========================================================================')
    print('Проверка с передачей аргументов по одному')
    assert check_path_from_syspath() == []
    assert check_path_from_syspath('C:\\GoogleDrive\\Python\\module_json') == [True]
    assert check_path_from_syspath('C:\\GoogleDrive\\Python\\practice_import_modules\\myapp') == [True]
    assert check_path_from_syspath('C:\\abracadabra') == [False]
    assert check_path_from_syspath('C:\\GoogleDrive\\abracadabra') == [False]
    
    
    print('\n\n✅ Все тесты пройдены')
