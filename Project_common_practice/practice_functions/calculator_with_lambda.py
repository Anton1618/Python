# Функция калькулятор
# Принимает на вход строку, содержащую два целых числа и один знак арифметической операции (+, -, /, *, **, //)
# Возвращает результат выполнения этой операции.
# Если числа не целые или нет знака операции, то должно быть возбуждено исключение ValueError

def calculator(expression):
    allowed = '+-/*'  # Допустимые значения для операций
    if not any(i in expression for i in
               allowed):  # Проверка наличия мат символов, в противном случае, применение функции не имеет смысла
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
                # По ТЗ - Если числа не целые или нет знака операции. Также относится к передаче "лишних" значений для вычислений, а также строк вместо числовых значений
                raise ValueError('Выражение должно содержать два целых числа и один знак')
                # Фиксирование побочных исключений
            except ZeroDivisionError:
                raise ZeroDivisionError('Нельзя делить на ноль')


if __name__ == '__main__':
    print(calculator('2+2'))
    print(calculator('2*0'))
    print(calculator('2/1'))
