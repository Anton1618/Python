'''
print-функции декорирующие текст

- Перехват stdout-потока и возвращение его как значения
- Декорирование заголовка в формате: '============ Hello, world! ============='
- Декорирование многоточием в формате: Hello, world!... 
'''

import functools
import sys
from io import StringIO

def capture_stdout(func, stripval='\n'):
    '''
    # Перехват вывода функции
    
    Перехватывает и возвращает поток функции stdout, который функция должна была отправить в консоль
    Для перехвата потока применяется временный строковый буфер io.StringIO
    

    ### Параметры
    - `func` - функция, stdout вывод которой необходимо перехватить
    - `strip` - один или множество символов для удаления, по умолчанию символа переноса строки. Буфер io.StringIO собирает данные и сохраняет их с разделителем - символом переноса строки

    
    ### Возвращаемое значение
    Возвращаемое значение функции - её вывод из потока stdout

    
    ### Примеры
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
    # Печать декорированных заголовков
    
    Функция принимает текст и выводит его в консоль в форматированном виде в установленном формате:
    - создается строка, с установленной длиной `string_width`
    - строка заполняется элементом `placeholder_character`
    - при достаточной длине строки, в ней размещается форматируемый элемент 
    - элемент может быть позиционирован в строке, располагаясь слева, справа или по центру
    - если ширина строки `string_width` меньше длины форматируемого элемента, то создается строка с элементом `placeholder_character`, равная длине форматируемого элемента, после которой на новой строке размещается сам форматируемый элемент

    
    ### Параметры
    - `format_elm` - Объект для форматирования, зачастую, строковый или числовой элемент, который декорируется
    - `string_width` - По умолчанию 120 символов. Числовое значение ширины строки, например: 10, 70, 140
    - `placeholder_character` - По умолчанию символ равно (=). Строковый элемент заполнитель, например: 'X', '~', '✨', '♥'
    - `positioning_symbol` - По умолчанию, размещение по центру. Строковый символ, обозначающий положение позиционирования объекта-форматирования в результирующей строке, например: '<' - слева, '^' - по центру, '>' - справа

    
    ### Возвращаемое значение
    Возвращаемое значение отсутствует, вместо этого, функция производит вывод результатов работы в стандартный поток вывода stdout
    

    ### Примеры:
    ```python
    pretty_header()  # ================================================================================
    pretty_header('Hello, world!', 1)  # ===============
                                        # Hello, world!
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
    # Многоточие для текста
    Функция добавляет к элементу `format_elm` многоточие
    
    ### Параметры:
    `format_elm` - любой элемент, который будет интерполирован в строку в формате "`format_elm`..."

    ### Примеры:
    ```python
    text_ellipsis()  # ...
    text_ellipsis(123)  # 123...
    text_ellipsis('Hello, world')  # Hello, world...
    text_ellipsis((1, 2, 3))  # (1, 2, 3)...
    ```
    '''
    print(f'\n{format_elm}...')




if __name__ == '__main__':
    # Для тестирования функций производится перехват их вывода
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


    print('\n\n✅ Все тесты пройдены')
