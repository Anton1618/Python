'''
Функция калькулятор
Принимает на вход строку, содержащую два целых числа и один знак арифметической операции (+, -, /, *, **, //)
Возвращает результат выполнения этой операции.
Если числа не целые или нет знака операции, то должно быть возбуждено исключение ValueError
'''

def calculate(expression):
    allowed = '+-/*'  # Допустимые значения для операций
    if not any(i in expression for i in allowed):  # Проверка наличия мат символов, в противном случае, применение функции не имеет смысла
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': (lambda a, b: a + b),
                    '-': (lambda a, b: a - b),
                    '*': (lambda a, b: a * b),
                    '/': (lambda a, b: round(a / b, 1))
                }[sign](left, right)
            except (ValueError, TypeError):
                # Если числа не целые или нет знака операции, 
                # Аргумент содержит излишние значения для вычислений
                # Наличие строк вместо числовых значений
                raise ValueError('Выражение должно содержать два целых числа и один знак')
            
                # Фиксирование побочных исключений
            except ZeroDivisionError:
                raise ZeroDivisionError('Нельзя делить на ноль')


if __name__ == '__main__':
    assert calculate('2/2') == 1.0
    assert calculate('2+2') == 4
    assert calculate('2*0') == 0
    assert calculate('2/1') == 2.0
    # calculate('2/0') # ZeroDivisionError: Нельзя делить на ноль
    print('Все тесты пройдены')
