'''Реализует строковый постфикс "год", "года" или "лет", в зависимости от числового значения.

Описание:
- "год", для чисел, которые оканчиваются на цифру 1.
- "года", для чисел, которые оканчиваются на цифру: 2, 3, 4.
- "лет", для чисел, которые оканчиваются на цифру: 0, 5, 6, 7, 8, 9
    И чисел, которые оканчиваются на число 11, 12, 13, 14;
'''


def get_suffix(age):
    if age % 100 in (11, 12, 13, 14):
        return f'{age} лет'
    n_age = age % 10
    if n_age == 1:
        return f'{age} год'
    elif n_age in (2, 3, 4):
        return f'{age} года'
    return f'{age} лет'


if __name__ == '__main__':
    assert get_suffix(0) == '0 лет'
    assert get_suffix(1) == '1 год'
    assert get_suffix(2) == '2 года'
    assert get_suffix(5) == '5 лет'
    assert get_suffix(10) == '10 лет'
    assert get_suffix(11) == '11 лет'
    assert get_suffix(12) == '12 лет'
    assert get_suffix(15) == '15 лет'
    assert get_suffix(20) == '20 лет'
    assert get_suffix(21) == '21 год'
    assert get_suffix(22) == '22 года'
    assert get_suffix(25) == '25 лет'
    assert get_suffix(100) == '100 лет'
    assert get_suffix(101) == '101 год'
    assert get_suffix(102) == '102 года'
    assert get_suffix(105) == '105 лет'
    assert get_suffix(110) == '110 лет'
    assert get_suffix(111) == '111 лет'
    assert get_suffix(112) == '112 лет'
    assert get_suffix(115) == '115 лет'
    assert get_suffix(120) == '120 лет'
    assert get_suffix(121) == '121 год'
    assert get_suffix(122) == '122 года'
    assert get_suffix(125) == '125 лет'


    print('\n\n✅ Все тесты пройдены')
