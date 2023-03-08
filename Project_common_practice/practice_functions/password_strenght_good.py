# Функция проверки пароля на сложность
# Под силой или сложностью пароля понимается его большее число разнообразных символов, которые входят в разные наборы
# -- Недостаточная длина пароля. Если пароль короче 8 символов, то вернуть Too Weak
# -- Содержит только один из наборов символов. Если пароль содержит только цифры, только строчные или только заглавные символы, то вернуть Weak
# -- Содержит два любых набора симвлов. Если пароль содержит символы любых 2 наборов, то вернуть Good
# -- Содержит наборы всех симвлов. Если пароль содержит символы всех наборов, то вернуть Very Good
from string import digits, ascii_lowercase, ascii_uppercase, punctuation

def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    count = 0 # Счетчик сложности пароля
    for symbols in (digits, ascii_lowercase, ascii_uppercase, punctuation):
        if any(i in symbols for i in value):
            count += 1 # Встречая символ, который входит в текущий итерируемый набор, увеличивается сложность пароля. Но это должно происходить только один раз за набор
            # Для корректного рассчета сложности пароля, необходим переход к новому набору из представленных, иначе сложность пароля превратиться в счетчик полученных значений
            continue # Поэтому после получения уникального значения, производится переход к следующему набору символов
    if count == 4: # Значение максимальной сложности пароля, которое может быть получено только при вхождении символов пароля во все наборы символов
        return 'Very Good'
    return 'Weak' if count==1 else 'Good'


if __name__ == '__main__':
    # Примерные аргументы, которые могут быть корректно обработаны программой. Буквально по несколько вариантов на тип возникающей ошибки
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('abcdefg') == 'Too Weak'
    assert password_strength('ABCDEFG') == 'Too Weak'
    assert password_strength('?*^`,/|') == 'Too Weak'
    assert password_strength('123qweQ') == 'Too Weak'
    assert password_strength('0987123424') == 'Weak'
    assert password_strength('asdfasfawega') == 'Weak'
    assert password_strength('ASDFASGASGA') == 'Weak'
    assert password_strength('?*^`,/|:\\"@&%$!-+') == 'Weak'
    assert password_strength('sadfsSGASGA') == 'Good'
    assert password_strength('1234SGASGA') == 'Good'
    assert password_strength('23432sdfsfsf') == 'Good'
    assert password_strength('^`,/|ASGASGA') == 'Good'
    assert password_strength('^`,/|sdfsdsd') == 'Good'
    assert password_strength('23sdsdfsdffSDFS*?') == 'Very Good'
    assert password_strength('!*@&sdfFDFSGSFsdf907') == 'Very Good'
    assert password_strength('AS|:\\"@&%DF45ASdsfsGA234SGA') == 'Very Good'
    # Если возникают какие-то исключения, то сначала добавляется assert, затем осуществляются изменения в коде
