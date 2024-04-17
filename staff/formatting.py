'''Функции форматирования создания строк с произвольным числом параметров''' 

def percent(*args: any, width_separ=1, val_separ=' ') -> str:
    '''Процентное форматирование'''
    format_string = ''

    for arg in args:
        match arg:
            case int():
                t_elm = 'd'
            case str():
                t_elm = 's'
            case collection if collection in (list, tuple, dict):
                t_elm = 'r'
        format_string += f'%{t_elm}{val_separ * width_separ}'
    
    return (format_string%args).rstrip(val_separ)


def format(*args: any, width_separ=1, val_separ=' '):
    '''Форматирование методом format'''
    format_string = (val_separ * width_separ).join('{}' for _ in range(len(args)))
    return format_string.format(*args)




if __name__ == '__main__':
    assert percent('a') == 'a'
    assert percent('a', 'b', 'c', width_separ=2) == 'a  b  c'
    assert percent(123, 'b', ['foo', 'bar', 'baz'], width_separ=2, val_separ='-') == "123--b--['foo', 'bar', 'baz']"

    assert format('a') == 'a'
    assert format('a', 'b', 'c', width_separ=2) == 'a  b  c'
    assert format(123, 'b', ['foo', 'bar', 'baz'], width_separ=2, val_separ='-') == "123--b--['foo', 'bar', 'baz']"


    print('\n\n✅ Все тесты пройдены')