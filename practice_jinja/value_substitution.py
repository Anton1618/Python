'''Шаблоны конструкций подстановки

{ %% } - Спецификатор шаблона
{{ value }} - Конструкция для вставки выражений на языке Python
'''
from jinja2 import Template

print(' Конструкция {{ value }} '.center(80, '-'))
print('Создание шаблона без подстановки значения')
tm = Template('hello, world')
msg = tm.render()
print(msg)  # hello, world
print()

print('Создание шаблона с подстановкой значения var в конструкцию {{ var }}')
tm = Template('hello, {{ var }} world')
msg = tm.render(var='beautiful')
print(msg)  # hello, beautiful world
print()

print('Создание шаблона с подстановкой значения var в конструкцию {% var %}')
tm = Template('hello, {{ var }} world')
msg = tm.render(var='beautiful')
print(msg)  # hello, beautiful world
print()

print('Создание шаблона с подстановкой значения var в конструкцию {{ var }}')
print()



# Подстановка простых данных
name = 'Anton'
age = 30

tm = Template('Hello, {{ name.upper() }}! You"re definitely {{ age }}?')
msg = tm.render(name=name, age=age)
print(msg)
'''Hello, ANTON! You"re definitely 30?'''


# Применение свойств класса, через обращение к полю и через обращение к гетеру
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self): # Гетер имени
        return self.name

anton = Person('anton', 30)
tm = Template('Hello, {{ anton.getName() }}! You"re definitely {{ anton.age }}?')
msg = tm.render(anton=anton) # Метод подставляет в шаблон значение переменной-аргумента, взамен той переменной, что была в шаблоне
print(msg)
'''Hello, anton! You"re definitely 30?'''


print(' Конструкция {{ value }} '.center(80, '-'))
