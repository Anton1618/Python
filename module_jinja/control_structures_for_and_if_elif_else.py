'''Управляющие конструкции for и if'''
# ====== Управляющая конструкция for ======
'''Управляющая конструкция for применяется для формирования списка на основе любого итерируемого объекта.
{%- for <выражение> %}
    <Инструкции на итерации цикла>
{%- endfor %}
Результирующими значениями станут построчно идущие проитерированные элементы.
Причем, ввиду применения тройных кавычек в конструкции, каждый перенос строки в конструкции будет отражен на результирующих элементах,
форматируя результат с наличием пустой строки на месте переноса строки.
Чтобы исключить лишние переносы строк из результата - применяется символ "-".
Он может быть установлен перед или после процента в управляющей конструкции, соответственно убирая лишние переносы строк.
'''
from jinja2 import Template

# Формирование списка HTML-опций на основе списка словарей Python
cities = [{'id': 1, 'city': 'Москва'},
            {'id': 15, 'city': 'Смоленск'},
            {'id': 23, 'city': 'Санкт-Петербург'},
            {'id': 48, 'city': 'Рязань'},
            {'id': 17, 'city': 'Тверь'}]

# На каждой итерации цикла станет осуществляться формирование опции, которая станет включать полученные данные id и названия города
# Доступание до элементов осуществляется простым обращением к каждому элементу коллекции
# Для размещения в опции необходимых значений, применяются двойные скобки подстановщика
# Для исключения из результата лишних переносов строк, применяется символ "-" перед процентом в первой и последней строке конструкции
link = '''<select name='cities'>
{%- for c in cities %}
    <option value='{{c['id']}}'>{{c['city']}}</option>
{%- endfor %}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
'''Результат:
<select name='cities'>
    <option value='1'>Москва</option>
    <option value='15'>Смоленск</option>
    <option value='23'>Санкт-Петербург</option>
    <option value='48'>Рязань</option>
    <option value='17'>Тверь</option>
</select>'''


# ====== Управляющая условная конструкция if/elif/else ======
'''Блок if выполняется при истинности заданного условия;
Если условие не выполняется, то поток выполнения переходит к проверке условия блока elif;
Если ни одно условие не выполнилось, то выполняется блок else.
Также поддерживает символ "-" для исключения лишних переносов строк.
{%- if <условие> %}
    <Инструкции, выполняемые при истинности условия>
{%- elif %}
    <Инструкции, выполняемые при ложности предыдущего блока>
{%- else %}
    <Инструкции, выполняемые при ложности всех прочих условий>
{%- endfile %}
'''

# Применение условной конструкции, для получения элементов, чей id больше 20
link = '''<select name='cities'>
{%- for c in cities %}
{%- if c.id > 20 %}
    <option value='{{c['id']}}'>{{c['city']}}</option>
{%- endif %}
{%- endfor %}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
'''Результат:
<select name='cities'>
    <option value='23'>Санкт-Петербург</option>
    <option value='48'>Рязань</option>
</select>'''

# Применение условной конструкции, для получения элементов, чей id больше 20.
# В противном случае - получение только названия города
link = '''<select name='cities'>
{%- for c in cities %}
{%- if c.id > 20 %}
    <option value='{{c['id']}}'>{{c['city']}}</option>
{%- else %}
    {{c['city']}}
{%- endif %}
{%- endfor %}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
'''Результат:
<select name='cities'>
    Москва
    Смоленск
    <option value='23'>Санкт-Петербург</option>
    <option value='48'>Рязань</option>
    Тверь
</select>'''

# Применение условной конструкции, для получения элементов, чей id больше 20,
# либо меньше 10, тогда значение сохраняется с добавленной припиской "опасной зоны".
# В противном случае - получение только названия города.
link = '''<select name='cities'>
{%- for c in cities %}
{%- if c.id > 20 %}
    <option value='{{c['id']}}'>{{c['city']}}</option>
{%- elif c.id < 10 %}
    <oprion value='{{c['id']}}>{{c['city']}} - В зоне риска</option>
{%- else %}
    {{c['city']}}
{%- endif %}
{%- endfor %}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
'''Результат:
<select name='cities'>
    <oprion value='1>Москва - В зоне риска</option>
    Смоленск
    <option value='23'>Санкт-Петербург</option>
    <option value='48'>Рязань</option>
    Тверь
</select>
'''