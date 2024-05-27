'''
# Функции форматироваия и отображения данных в консоль


## Список функций
- `capture_stdout`: Перехват stdout-потока и возвращение его как значения
- `pretty_header`: print-функция для декорирования заголовка в формате: '============ Hello, world! ============='
- `text_ellipsis`: print-функция для декорирования многоточием в формате: Hello, world!...
- `percent`: Процентное форматирование
- `mformat`: Форматирование методом формат
- `db_table_print`: print-функция для отображения данный БД в виде таблицы
'''

import functools
import sys
from io import StringIO

def capture_stdout(func, stripval: str='\n'):
    '''
    # Перехват stdout-потока и возвращение его как значения

    Перехватывает и возвращает поток функции stdout, который функция должна была отправить в консоль
    Для перехвата потока применяется временный строковый буфер `io.StringIO`


    ## Параметры
    - `func` (function): функция, stdout-вывод которой необходимо перехватить
    - `stripval` (str): один или множество символов для удаления, по умолчанию символа переноса строки.
    Буфер `io.StringIO` собирает данные и сохраняет их с разделителем - символом переноса строки


    ## Возвращаемое значение
    Возвращаемое значение функции - это в первую очередь перехваченный вывод обрабатываемой функции, а также, возвращаемое значение этой функции, если таковой предполагается


    ## Примеры
    ```python
    @capture_stdout
    def foo1():
        print('Перехваченный вывод')
    assert foo1() == 'Перехваченный вывод'

    @capture_stdout
    def foo2():
        print('Первый перехваченный вывод')
        print('Второй перехваченный вывод')
    assert foo2() == 'Первый перехваченный вывод\nВторой перехваченный вывод\n'
    ```
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        captured_output = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            result = func(*args, **kwargs)
            if result:
                return captured_output.getvalue().strip(stripval), result
            return captured_output.getvalue().strip(stripval)
        finally:
            sys.stdout = original_stdout
    return wrapper




def pretty_header(format_elm: any='', string_width: int=80, placeholder_character: str="=", positioning_symbol: str='^'):
    '''
    # print-функция для декорирования заголовка

    Функция принимает текст и выводит его в консоль в форматированном виде в установленном формате:
    - создается строка, с установленной длиной `string_width`
    - строка заполняется элементом `placeholder_character`
    - при достаточной длине строки, в ней размещается форматируемый элемент 
    - элемент может быть позиционирован в строке, располагаясь слева, справа или по центру
    - если ширина строки `string_width` меньше длины форматируемого элемента, то создается строка с элементом `placeholder_character`, равная длине форматируемого элемента, после которой на новой строке размещается сам форматируемый элемент


    ## Параметры
    - `format_elm` (any): Объект для форматирования, зачастую, строковый или числовой элемент, который декорируется
    - `string_width` (int): По умолчанию 120 символов. Числовое значение ширины строки, например: 10, 70, 140
    - `placeholder_character` (str): По умолчанию символ равно (=). Строковый элемент заполнитель, например: 'X', '~', '✨', '♥'
    - `positioning_symbol` (str): По умолчанию, размещение по центру. Строковый символ, обозначающий положение позиционирования объекта-форматирования в результирующей строке, например: '<' - слева, '^' - по центру, '>' - справа


    ## Возвращаемое значение
    Результат работы функции выводится в стандартный поток вывода stdut


    ## Примеры:
    ```python
    pretty_header()  # ================================================================================
    pretty_header('Hello, world!', 1)  # ===============
    #                                     Hello, world!
    pretty_header('Hello, world!', 40)  # ============ Hello, world! =============
    pretty_header('Hello, world!', 40, '~')  # ~~~~~~~~~~~~ Hello, world! ~~~~~~~~~~~~~
    pretty_header('Hello, world!', 40, '~', '>')  # ~~~~~~~~~~~~~~~~~~~~~~~~~ Hello, world!
    ```
    '''
    if format_elm:
        format_elm = ' ' + str(format_elm) + ' '

    print(f'{placeholder_character * len(format_elm) if string_width < len(format_elm) else ''}' +
        f'\n{format_elm:{placeholder_character}{positioning_symbol}{string_width}}')




def text_ellipsis(format_elm: any=''):
    '''
    # print-функция форматирования, добавляющая постфикс многоточия


    ## Параметры
    `format_elm` (any): любой элемент, который будет интерполирован в строку в формате "format_elm..."


    ## Возвращаемое значение
    Результат работы функции выводится в стандартный поток вывода stdut


    ## Примеры
    ```python
    text_ellipsis()  # ...
    text_ellipsis(123)  # 123...
    text_ellipsis('Hello, world')  # Hello, world...
    text_ellipsis((1, 2, 3))  # (1, 2, 3)...
    ```
    '''
    print(f'\n{format_elm}...')




def percent(*args: any, width_separ: int=1, val_separ: str=' ') -> str:
    '''
    # Функция процентного форматирования 

    Принимает переменное число аргументов и возвращает отформатированную строку


    ## Параметры
    - `*args` (any): переменное число аргументов для интерполяции в строку
    - `width_separ` (int): значение разделителя между форматируемыми элементами
    - `val_separ` (str): значение заполнителя в `width_separ`


    ## Возвращаемое значение
    Функция возвращает строку со всеми интерполированными значениями, которые были переданы для форматирования


    ## Примеры
    ```python
    percent('a')  # 'a'
    percent('a', 'b', 'c', width_separ=2)  # 'a  b  c'
    percent(123, 'b', ['foo', 'bar', 'baz'], width_separ=2, val_separ='-')  # "123--b--['foo', 'bar', 'baz']"
    ```
    '''
    format_string = ''

    for arg in args:
        match arg:
            case integer if integer in (int, float):
                t_elm = 'd'
            case str():
                t_elm = 's'
            case _:
                t_elm = 'r'
        format_string += '%' + t_elm + (val_separ * width_separ)

    return (format_string%args).rstrip(val_separ)




def mformat(*args: any, width_separ: int=1, val_separ: str=' ') -> str:
    '''
    # Функция форматирования методом .format

    Принимает переменное число аргументов и возвращает отформатированную строку


    ## Параметры
    - `*args` (any): переменное число аргументов для интерполяции в строку
    - `width_separ` (int): значение разделителя между форматируемыми элементами
    - `val_separ` (str): значение заполнителя в `width_separ`


    ## Возвращаемое значение
    Функция возвращает строку со всеми интерполированными значениями, которые были переданы для форматирования


    ## Примеры
    ```python
    percent('a')  # 'a'
    percent('a', 'b', 'c', width_separ=2)  # 'a  b  c'
    percent(123, 'b', ['foo', 'bar', 'baz'], width_separ=2, val_separ='-')  # "123--b--['foo', 'bar', 'baz']"
    ```
    '''
    format_string = (val_separ * width_separ).join('{}' for _ in range(len(args)))
    return format_string.format(*args)




def db_table_print(columns: tuple[tuple[str]], data: list[tuple[str]], table_width: int=75):
    '''
    # print-функция отображения данных БД в консоли


    ## Параметры
    - `columns` (tuple[tuple[str]]):  кортеж кортежей со строками. Объект данных должен быть получен пользователем из стандартного объекта курсора, командой `cursor.description`. Функция получит из него 0-элемент - название последнего обрабатываемого столбца
    - `data` (list[tuple[str]]): список кортежей строк. Объект данных должен быть получен пользователем из стандартного объекта курсора, например командой `cursor.fetchall()`.
    При этом, отображены будут все полученные данные!!!
    Поэтому, если необходимо ограничить отображение, может быть получена определенная выбора, например, с применением в команде диапазонов `cursor.fetchall()[:10]`, для получения данных из таблицы в 10 записей
    - `table_width` (int): общее значение ширины таблицы


    ## Возвращаемое значение
    Результат работы функции выводится в стандартный поток вывода stdut


    ## Примеры
    ```python
    columns = ['product_title', 'price', 'customer_names', 'manager_names']
    data = [('Смартфон Google Pixel 7 8/256GB Black', 61000, 'Светлана Назарова', 'Эмилия Куликова'),
    ('Планшет Xiaomi Redmi Pad SE 4/128GB Gray (49283)', 16000, 'Анастасия Капустина', 'Назар Русаков')]
    
    print(db_table_print(columns, data, 80))
    #    
    # -------------------------------------------------------------------------------- 
    # |product_title      |price              |customer_names     |manager_names      |
    # -------------------------------------------------------------------------------- 
    # |Смартфон Google ...|61000              |Светлана Назарова  |Эмилия Куликова    |
    # |Планшет Xiaomi R...|16000              |Анастасия Капустина|Назар Русаков      |
    # -------------------------------------------------------------------------------- 
    ```
    '''
    columns = [elm[0] for elm in columns]
    def template(elms, position='<'):
        count = len([*elms])
        col_width = (table_width // count) - 2
        s = ' {:{p}{w}}|' * count
        def correct_elm(e):
            return se if len(se:=str(e)) <= col_width else se[:col_width-3] + '...'
        return '|' + s.format(*[correct_elm(elm) for elm in [*elms]], w=col_width, p=position)

    print()
    print('-' * table_width)
    print(template(columns, '<'))
    print('-' * table_width)
    for line in data:
        print(template(line))
    print('-' * table_width)
    print()




if __name__ == '__main__':
    # Для тестирования print-функций производится перехват их stduut-вывода
    pretty_header = capture_stdout(pretty_header)
    text_ellipsis = capture_stdout(text_ellipsis)


    assert pretty_header() == '================================================================================'
    assert pretty_header('Hello, world!', 10) == '===============\n Hello, world! '
    assert pretty_header('Hello, world!', 40) == '============ Hello, world! ============='
    assert pretty_header('Hello, world!', 40, '~') == '~~~~~~~~~~~~ Hello, world! ~~~~~~~~~~~~~'
    assert pretty_header('Hello, world!', 40, '~', '>') == '~~~~~~~~~~~~~~~~~~~~~~~~~ Hello, world! '


    assert text_ellipsis() == '...'
    assert text_ellipsis(123) == '123...'
    assert text_ellipsis('Hello, world') == 'Hello, world...'
    assert text_ellipsis((1, 2, 3)) == '(1, 2, 3)...'


    assert percent('a') == 'a'
    assert percent('a', 'b', 'c', width_separ=2) == 'a  b  c'
    assert percent(123, 'b', ['foo', 'bar', 'baz'], width_separ=2, val_separ='-') == "123--b--['foo', 'bar', 'baz']"


    assert mformat('a') == 'a'
    assert mformat('a', 'b', 'c', width_separ=2) == 'a  b  c'
    assert mformat(123, 'b', ['foo', 'bar', 'baz'], width_separ=2, val_separ='-') == "123--b--['foo', 'bar', 'baz']"


    print('\n\n✅ Все тесты пройдены')
