'''Переопределение методов __str__, __add__ и __mull__

Описание:
- values - управляемое свойство элементов объекта
    геттер - возвращает значения в отсортированном виде
    сеттер - валидатор, проверяющий элементы на корректность. Элементами могут быть только целочисленные значения
- str - отображение данных в пользовательском формате
- add - сложение значений вектора с переданным аргументом
- mul - умножение значений вектора с переданным аргументом
'''

class Vector:
    def __init__(self, *args):
        self._values = args
    @property
    def values(self):
        return sorted(self._values)
    @values.setter
    def values(self, new_values):
        for i in new_values:
            if not isinstance(i, int):
                raise ValueError('Значениями могут быть только целочисленные элементы')
        self._values = new_values

    def __str__(self):
        if self.values:
            st = '<{}> ' * len(self.values)
            return f"Вектор: {st.format(*self.values)}"
        else:
            return f'Вектор пуст'

    def __add__(self, other):
        '''Суммирование значений и реализация в новом объекте класса
        - Если аргумент число, реализация осуществляется суммированием каждого значения вектора с полученным аргументом
        - Если аргументом является объект этого класса, то осуществляется позиционное суммирование значений одного
         вектора со значениями другого'''
        if isinstance(other, int):
            sum_vector = [i + other for i in self.values]
        elif isinstance(other, self.__class__):
            sum_vector = []
            greatest, least = (self.values, other.values) if len(self.values) > len(other.values) else (other.values, self.values)
            for i in range(len(least)):
                sum_vector.append(least[i] + greatest[i])
            else:
                sum_vector.extend(greatest[i+1:])
        else:
            raise ValueError(f'Суммирование с элементом {other} невозможно.\n'
                             f'Аргумент должен быть числом или объектом класса {self.__class__.__name__}')
        return self.__class__(*sum_vector)


if __name__ == '__main__':
    print('Построение и отображение значений векторов')
    v1 = Vector(1, 2, 3)
    v2 = Vector(30, 10, 20, 40, 50, 60)
    v3 = Vector()
    print('Состав векторов')
    print(v1)
    print(v2)
    print(v3)
    print()

    print('Создание результирующего объекта с суммой значений')
    print('Прибавление целочисленного значения ко всем элементам вектора')
    sumVector1 = v1 + 10
    print(type(sumVector1), sumVector1)
    print('Сложение элементов векторов')
    sumVector2 = v1 + v2
    print(type(sumVector2), sumVector2)
    print('Ошибочная передача аргумента, не относящегося к целочисленному типу или объекту класса Vector')
    # sumVector3 = v1 + 'abracadabra' # ValueError: Суммирование с элементом abracadabra невозможно.
    # Аргумент должен быть числом или объектом класса Vector
    print()