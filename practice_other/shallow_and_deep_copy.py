'''Поверхностная и глубокая копии в Python

Применяются отображения исходного объекта и объектов его копий
'''
print()
list_a = [1, 2, 3, [10, 20]]
print(f'Исходный объект: {list_a=}')
print()


print(' Создание поверхностных (Shallow) копий и отображение id элементов в них '.center(80, '-'))
list_b = list(list_a)
list_b2 = sorted(list_a, key=lambda i: i if isinstance(i, int) else i[0])
list_b3 = list_a.copy()
list_b4 = list_a[:]
list_b5 = [*list_a]
list_b6 = [letter for letter in list_a]
print('Если в исходном списке есть вложенные объекты, например, другой список, то новый список будет содержать '
      'ссылки на те же вложенные объекты')
print(f'Исходный объект:')
print(f'{list_a=}')
print('id элементов исходного объекта:')
print(*[id(i) % 10000 for i in list_a])
print()
print('Объекты копии:')
print(f'{list_b=}\n'
      f'{list_b2=}\n'
      f'{list_b3=}\n'
      f'{list_b4=}\n'
      f'{list_b5=}\n'
      f'{list_b6=}')
print('id элементов объекта-копии идентичны с исходным объектом:')
print('\n'.join([' '.join([str(id(j) % 10000) for j in i]) for i in [list_b, list_b2, list_b3, list_b4, list_b5, list_b6]]))
print()


print(' Внесение различных изменений '.center(80, '-'))
print('- Изменение элемента на первом уровне вложенности в исходном объекте или одной из его копий, не отразится на '
      'прочих объектах и станет относиться только к этому конкретному объекту')
list_a[0] = 42
list_b[1] = 42
print('- По аналогичному принципу, внесение нового элемента в исходный объект, не отразится на объектах копиях, '
      'ввиду того, что ссылка не этот элемент не была скопирована')
list_a.append([100, 200, 300])
print('- Изменение вложенного элемента в исходном объекте или одной из его копий, отразиться на всех прочих объектах, '
      'ссылающихся на этот элемент')
list_a[3][0] = 'hello'
list_b6[3][1] = 'world'
print()


print(' Отображение элементов после изменений '.center(80, '-'))
print(f'Исходный объект:')
print(f'{list_a=}')
print('id элементов исходного объекта:')
print(*[id(i) % 10000 for i in list_a])
print()
print('Объекты копии:')
print(f'{list_b=}\n'
      f'{list_b2=}\n'
      f'{list_b3=}\n'
      f'{list_b4=}\n'
      f'{list_b5=}\n'
      f'{list_b6=}')
print('id элементов объекта-копии:')
print('\n'.join([' '.join([str(id(j) % 10000) for j in i]) for i in [list_b, list_b2, list_b3, list_b4, list_b5, list_b6]]))
print()


print(' Создание глубоких (Deep) копий и отображение id элементов в них '.center(80, '-'))
import copy
print('Состав объектов:')
list_c = copy.deepcopy(list_a)
print(f'{list_a=}', f'{list_c=}', sep='\n')
print()

print('Ссылки на элементы объектов:')
print('\n'.join([' '.join([str(id(j) % 10000) for j in i]) for i in [list_a, list_c]]))
print()

print('Внесение изменений и отображение ссылок на элементы:')
list_a[3][0] = 'Python'
list_c[3][1] = 'Qwerty'
print('\n'.join([' '.join([str(j) for j in i]) for i in [list_a, list_c]]))
print('\n'.join([' '.join([str(id(j) % 10000) for j in i]) for i in [list_a, list_c]]))
