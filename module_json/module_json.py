'''Демонстрация работы функций сериализации и десериализации модуля json'''

import json

print('-'.center(80, '-'))
print('dump() - Сериализация Python объекта в JSON файл (Python obj -> JSON file)\n'
      'dumps() - Сериализация Python объекта в JSON строку (Python obj -> JSON str)')

print('- Простая сериализация')
data = {"name": "John", "age": 30, "city": "New York"}
with open('data.json', 'w') as file:
    json.dump(data, file)

print(json.dumps(data))
# '{"name": "John", "age": 30, "city": "New York"}'
print()


print('- Сериализация с отступами')
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print(json.dumps(data, indent=4))
# '{\n    "name": "John",\n    "age": 30,\n    "city": "New York"\n}'
print()


print('- Сериализация несериализуемого объекта')
print('Для сериализации применяется преобразование функциональным объектом')
unserializable_data = {"name": "John", "age": 30, "city": "New York", "obj": object()}
with open('data.json', 'w') as file:
    json.dump(unserializable_data, file, default=str)

print(json.dumps(unserializable_data, default=str))
# '{"name": "John", "age": 30, "city": "New York", "obj": "<object object at 0x00000297F33B4390>"}'
print()


print('- Сериализация пользовательского объекта')
print('Для сериализации применяется класс-кодировщик, наследуемый от JSONEncoder')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

person = Person('John', 30)
with open('data.json', 'w') as file:
    json.dump(person, file, cls=PersonEncoder)

print(json.dumps(person, cls=PersonEncoder))
# '{"name": "John", "age": 30}'
print()
print()


print('-'.center(80, '-'))
print('load() - Десериализация JSON файла в Python объект  (JSON file -> Python obj)\n'
      'loads() - Десериализация JSON строки в Python объект (JSON str -> Python obj)')

print('- Простая десериализация')
with open('data.json', 'r') as file:
    data = json.load(file)

data_str = '{"name": "John", "age": 30}'
print(json.loads(data_str))
# {"name": "John", "age": 30}
print()


print('- Десериализация с применением пользовательской функции')
def object_hook(obj):
    return {k: v for k, v in obj.items()}

with open('data.json', 'r') as file:
    data = json.load(file, object_hook=object_hook)

data_str = '{"name": "John", "age": 30}'
print(json.loads(data_str, object_hook=object_hook))
# {'name': 'John', 'age': 30}
print()


print('- Десериализация с изменением типа чисел')
with open('data.json', 'r') as file:
    data = json.load(file, parse_float=float, parse_int=int)

data_str = '{"name": "John", "age": 30.0, "strange_num": 0.00001}'
print(json.loads(data_str, parse_float=float, parse_int=int))
# {'name': 'John', 'age': 30.0, 'strange_num': 1e-05}
print()


print('- Десериализация с применением пользовательского и встроенного классов')
print('Из файла')
print('С пользовательским классом')
class MyDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        return super().decode(s)

with open('data.json', 'r') as file:
    data = json.load(file, cls=MyDecoder)

print('С встроенным классом')
my_decoder = json.JSONDecoder()
with open('data.json', 'r') as file:
    data_str = file.read()
    data = my_decoder.decode(data_str)

print('Из строки')
data_str = '{"name": "John", "age": 30, "city": "New York"}'
print(json.loads(data_str, cls=MyDecoder))
# {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_decoder.decode(data_str))
# {'name': 'John', 'age': 30, 'city': 'New York'}
print()


print('- Сравнение параметров object_hook, принимающего словарь и object_pairs_hook, принимающего спискок двуэлементных '
      'кортежей')
print('Учитывая, что ключами являться только строки, их можно преобразовывать, например в верхний регистр')
print('Параметр object_pairs_hook')
def object_pairs_hook(obj):
    return {k.upper(): v for k, v in obj}

with open('data.json', 'r') as file:
    data = json.load(file, object_pairs_hook=object_pairs_hook)

print(json.loads(data_str, object_pairs_hook=object_pairs_hook))
# {'NAME': 'John', 'AGE': 30}
print()

print('Параметр object_hook')
def object_hook(obj):
    return {k.upper(): v for k, v in obj.items()}

with open('data.json', 'r') as file:
    data = json.load(file, object_hook=object_hook)

print(json.loads(data_str, object_hook=object_hook))
# {'NAME': 'John', 'AGE': 30}


