'''Сравнение форм записи генераторов

- generator expression: (elm for elm in iterable).
Генератор, вида представление коллекции, возвращает объект-генератор <genexpr>.

- generator function: def func(): yield.
Пользовательская (генераторная) функция, в теле которой присутствует оператор yield
'''

square1 = (i ** 2 for i in range(0, 11, 2))


def square2():
    for i in range(0, 11, 2):
        yield i ** 2

def pause():
    print('Начало работы генератора')
    while value < 100:
        print(f'Значение переменной до yield: {value}')
        yield f'Значение переменной, возвращаемое yield: {value}'
        print(f'Значение переменной после yield: {value}')
    else:
        print('Завершение работы генератора')


if __name__ == '__main__':
    print('Генераторное выражение')
    print(square1)
    print(f'Атрибуты объекта-генератора: \n{dir(square1)}')
    print('Вычисление')
    for i in square1:
        print(i, end=' ')
    # 0 4 16 36 64 100
    print()
    print()

    print('Генераторная функция')
    gen = square2()
    print(gen)
    print(f'Атрибуты генераторной функции: \n{dir(square2)}')
    print(f'Атрибуты объекта-генератора: \n{dir(gen)}')
    print('Вычисление')
    for i in gen:
        print(i, end=' ')
    # 0 4 16 36 64 100
    print()
    print()

    print('Способность генератора запоминать состояние локальных переменных позволяет применять его для сложных, '
          'например, глобальных и изменяющихся условий вне генератора')
    print('Последовательное выполнение инструкций, реализует:\n'
          '- один вывод строки "Generator working..."\n'
          '- последовательно выполняемые инструкции вечного цикла, которые берут значение переменной из глобальной '
          'области видимости\n'
          '- т.е. на каждой итерации берется значение глобальной переменной, фиксируется в генераторе и затем '
          'возвращается\n')
    value = 50
    gen_pause = pause()
    print(next(gen_pause))
    value = 100
    # print(next(gen_pause))  # ? (StopIteration)
    value = 250
    # print(next(gen_pause))  # ? (StopIteration)
