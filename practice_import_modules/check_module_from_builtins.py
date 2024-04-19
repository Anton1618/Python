'''Различные полезные функции'''

def check_module_from_builtins(*modules) -> list[bool]:
    '''# Проверка наличия модуля во встроенном пространстве имен builtin_module_names
    
    Наименования для проверки добавляются ключами в словарь, где, изначально, значениями для этих ключей устанавливается False.
    При истинности проверки, значение False будет изменено на значение True
    

    ## Параметры
    `modules`: одна или множество строк наименований модулей для проверки. 'sys' или 'sys', 'time'


    ## Возвращаемое значение
    `list[bool]`: список результатов на логическую проверку 


    ## Примеры
    ```python
    check_module_from_builtins()  # []
    check_module_from_builtins('sys')  # [True]
    check_module_from_builtins('sys', 'abracadabra')  # [True, False]
    ```
    '''
    from sys import builtin_module_names

    target_modules = {name:False for name in modules}

    for module in builtin_module_names:
        if module in target_modules:
            target_modules[module] = True
    
    for st, val in target_modules.items():
        print(f'{val!r:<6}: {st}')

    return list(target_modules.values())




if __name__ == '__main__':
    assert check_module_from_builtins() == []
    assert check_module_from_builtins('sys') == [True]
    assert check_module_from_builtins('abracadabra') == [False]
    assert check_module_from_builtins('sys', 'abracadabra') == [True, False]
    
    
    print('\n\n✅ Все тесты пройдены')
