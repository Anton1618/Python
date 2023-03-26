def calculate(a:int, b:int, operation:str) -> int | str:
    match operation:
        case '+':
            return a+b
        case '-':
            return a-b
        case '/':
            if b == 0:
                return 'Нельзя делить на ноль'
            return a//b
        case '*':
            return a*b
        case _:
            return f'Неизвестная операция'


if __name__ == '__main__':
    assert calculate(10, 2, '/') == 5
    assert calculate(3, 3, '*') == 9
    assert calculate(10, 0, '-') == 10
    assert calculate(-1, 0, '+') == -1
    assert calculate(1, 0, '/') == 'Нельзя делить на ноль'
    assert calculate(1, 1, '//') == 'Неизвестная операция'
    assert calculate(1, 2, '**') == 'Неизвестная операция'
    assert calculate(1, 2, '^') == 'Неизвестная операция'
    assert calculate(1, 2, '%') == 'Неизвестная операция'
    print('Все тесты пройдены')
