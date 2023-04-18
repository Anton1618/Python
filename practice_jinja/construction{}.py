'''Формирование шаблонов и конструкции подстановки значений:
{%%} - Спецификатор шаблона
{{}} - Выражение для вставки конструкции на языке Python в шаблон
{##} - Блок комментариев
# ## - Строковый комментарий
'''
from jinja2 import Template


# Создание шаблона без подстановки значения
tm = Template('hello, world')
msg = tm.render()
print(msg)
'''hello, world'''


# Создание шаблона с подстановкой значения
tm = Template('hello, {{ var }} world') # Формирование строки на основе класса, заключаемое в класс
# Метод render подставляет значение именованного аргумента-переменной взамен одноименной переменной в шаблоне, на манер методов форматирования
msg = tm.render(var='beautiful')
print(msg) # Результатом подстановки является обработанный шаблон, с подставленным значением
'''hello, beautiful world'''


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