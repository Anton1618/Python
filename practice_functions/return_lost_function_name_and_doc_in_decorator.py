'''Сохранение имени функции и её документации при декорировании'''
from functools import wraps


def HTMLdecor(func):
    '''Декоратор, в котором не предусмотрено сохранение имени функции и её документации'''
    def inner(*args, **kwargs):
        return '<h1>\n' \
               f'{func(*args, **kwargs)}\n' \
               f'</h1>\n'
    return inner


def HTMLdecorManualMeta(func):
    '''Декоратор, в котором для его замыкания вручную присвоены атрибуты декорируемой функции'''
    def inner(*args, **kwargs):
        return '<h1>\n' \
               f'{func(*args, **kwargs)}\n' \
               f'</h1>\n'
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

def HTMLdecorAutoMeta(func):
    '''Декоратор, в котором для его замыкания применяется декоратор wraps, автоматически передающий атрибуты
    декорируемой функции'''
    @wraps(func)
    def inner(*args, **kwargs):
        return '<h1>\n' \
               f'{func(*args, **kwargs)}\n' \
               f'</h1>\n'
    return inner


def SaleFunc(product, price):
    '''Декорируемая функция. Возвращает наименование акционного товара и его цену'''
    return f'Sale of {product} by {price}'


func_without_meta = HTMLdecor(SaleFunc)
func_with_man_meta = HTMLdecorManualMeta(SaleFunc)
func_with_auto_meta = HTMLdecorAutoMeta(SaleFunc)


if __name__ == '__main__':
    print('Декорируемая функция')
    print(f'Документация: {SaleFunc.__doc__}')  # Декорируемая функция. Возвращает наименование акционного товара и его цену
    print(f'Имя функции: {SaleFunc.__name__}')  # SaleFunc
    print()

    print('По умолчанию, декорируемая функция теряет свои имя и документацию при декорировании\n'
          'Вместо них будут применяться имя и документация замыкания декоратора')
    print(f'Документация замыкания: {func_without_meta.__doc__}')
    # None
    print(f'Имя замыкания: {func_without_meta.__name__}')
    # inner
    print()

    print('Для сохранения документации и имени декорируемой функции')
    print('- Aтрибуты могут быть вручную присвоены замыканию декоратора')
    print(f'Документация декорируемой функции: {func_with_man_meta.__doc__}')
    # Декорируемая функция. Возвращает наименование акционного товара и его цену
    print(f'Имя декорируемой функции: {func_with_man_meta.__name__}')
    # SaleFunc
    print()

    print('- Атрибуты могут быть автоматически переданы замыканию, если применить на нем декоратор wraps')
    print(f'Документация декорируемой функции: {func_with_auto_meta.__doc__}')
    # Декорируемая функция. Возвращает наименование акционного товара и его цену
    print(f'Имя декорируемой функции: {func_with_auto_meta.__name__}')
    # SaleFunc
    print()









