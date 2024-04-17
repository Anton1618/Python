'''
# Применение атрибутов функций



## Сохранение и получение значений между вызовами функции
Сохранение и получение значений между вызовами функции позволякт функциям сохранять результаты или состояния, полученные в предыдущих вызовах, для использования в последующих вызовах
Это полезно для функций, которым нужно "запоминать" некоторую информацию или результаты, для повышения производительности



## Динамическое изменение атрибутов, при каждом вызове функции
### Базовая cтруктура
Исходя из необходимости динамического изменения значений у атрибута, значение не должно зависеть от своего начального состояния, поэтому, вместо инициализации в инструкциях целевой функции, оно должно быть объявлено снаружи и ДО вызова 
целевой функции, в инструкциях которой станет изменяться необходимый атрибут


### Объединение или инкапсуляция
Первоначальное состояние необходимого атрибута может быть вынесено во внешнее пространство, например, в рамках конструкции замыкания, декоратора, которые станут включать всю необходимую логику в одном функциональном объекте
При этом, можно контралировать возможность изменения атрибута в возвращаемой функции (функции-замыкании)

- Инкапсулировать, если необходимо защитить атрибут от возможности прямого изменения.
Целевой атрибут может быть присвоен родительской функции, что позволит ограничить доступ к нему, так как вложенная фукнция-замыкание только станет применять его значение в своих инструкциях, но не обладать им

- Только объединить логику, если необходимо сохранить возможность прямого изменения.
Целевой атрибут может быть присвоен вложенной функции, что позволит обращаться к нему напрямую и изменять при необходимости
'''

from staff import printing
import time


def metadata(attr):
    '''Определение атрибутов вне тела функции'''
    return getattr(metadata, attr)
metadata.version = '0.1.6'
metadata.author = 'Владимир Прохоров'


def add_item(item):
    '''Сохранение полученных значений'''
    if 'items' not in dir(add_item):
        add_item.items = []
    add_item.items.append(item)
    return add_item.items


def expensive_computation(x):
    '''Сохранение полученных значений и кэширование вычислений'''
    if 'cache' not in dir(expensive_computation):
        expensive_computation.cache = {}
    if x not in expensive_computation.cache:
        print('Производятся тяжелые вычисления')
        expensive_computation.cache[x] = x * x
    return expensive_computation.cache[x]


def trottling_function(cooldown=1):
    '''Троттлинг функции через замыкание'''
    trottling_function.last_call = time.time() - cooldown
    def trottling():
        current_time = time.time()
        if current_time - trottling_function.last_call < cooldown:
            return 'Ожидайте...'
        trottling_function.last_call = current_time
        return 'Выполнение...'
    return trottling




if __name__ == '__main__':
    # Для expensive_computation применяется перехват вывода, из за чего в демонстрации возвращаемое значение представлено кортежем из двух элементов
    expensive_computation = printing.capture_stdout(expensive_computation)
    
    assert metadata('author') == 'Владимир Прохоров'
    assert metadata('version') == '0.1.6'


    assert add_item(1) == [1]
    assert add_item(2) == [1, 2]
    assert add_item('foo') == [1, 2, 'foo']


    assert expensive_computation(10)  ==  ('Производятся тяжелые вычисления', 100)
    assert expensive_computation(10) == ('', 100)
    assert expensive_computation(20)  == ('Производятся тяжелые вычисления', 400)
    

    tr_func = trottling_function(5)
    assert tr_func() == 'Выполнение...'
    assert tr_func() == 'Ожидайте...'
    assert tr_func() == 'Ожидайте...'
    tr_func = trottling_function(1)
    assert tr_func() == 'Выполнение...'
    time.sleep(1)
    assert tr_func() == 'Выполнение...'
    time.sleep(1)
    assert tr_func() == 'Выполнение...'


    print('\n\n✅ Все тесты пройдены')
