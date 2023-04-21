'''Переопределение методов __str__, __add__ и __mull__

Описание:
- values - управляемое свойство элементов объекта
    - геттер - возвращает значения в отсортированном виде
    - сеттер - валидатор, проверяющий элементы на корректность. Элементами могут быть только целочисленные значения
- str - отображение данных в пользовательском формате
- add - сложение значений вектора с переданным аргументом
- mul - умножение значений вектора с переданным аргументом
'''

class Vector:
    def __init__(self, *args):
        self.values = args
    @property
    def values(self):
        return sorted(self._values)
    @values.setter
    def values(self, new_values):
        if not all([isinstance(i, int) for i in new_values]):
            raise ValueError('Значениями могут быть только целочисленные элементы')
        self._values = new_values
    def __repr__(self):
        return f'<vr {id(self) % 1000!r}>'
    def __str__(self):
        comp = (r"<{}> " * len(self.values)).format(*self.values) if self.values else 'пуст'
        return f'{repr(self)}: {comp}'

    def __add__(self, other):
        '''Суммирование значений и реализация в новом объекте класса
        - Если аргументом является число, то для каждого значения вектора, осуществляется приращение на его значение.
        - Если аргументом является другой объект-вектор, то для каждого значения текущего, осуществляется позиционное
        приращение на значения другого.
        При этом, если векторы разной длины, то оставшиеся элементы наибольшего вектора, будут добавлены в массив текущего.
        Таким образом, любое сложение векторов приводит к получению вектора наибольшей длины'''
        if isinstance(other, int):
            return self.__class__(*[i + other for i in self.values])
        elif isinstance(other, self.__class__):
            sum_vector = []
            greatest, least = (self.values, other.values) if len(self.values) > len(other.values) else (other.values, self.values)
            i = 0
            while i < len(least):
                sum_vector.append(least[i] + greatest[i])
                i += 1
            return self.__class__(*sum_vector + greatest[i:])
        else:
            raise ValueError(f'Суммирование с элементом {other} невозможно.\n'
                             f'Аргумент должен быть числом или объектом класса {self.__class__.__name__}')
    def __mul__(self, other):
        '''Метод полностью аналогичен __add__, но выполняет умножение элементов вектора, вместо их сложения,
        для аналогичного получения нового объекта вектора по наибольшей длине операндов'''
        if isinstance(other, int):
            return self.__class__(*[i * other for i in self.values])
        elif isinstance(other, self.__class__):
            mul_vector = []
            greatest, least = (self.values, other.values) if len(self.values) > len(other.values) else (other.values, self.values)
            i = 0
            while i < len(least):
                mul_vector.append(least[i] * greatest[i])
                i += 1
            return self.__class__(*mul_vector + greatest[i:])
        else:
            raise ValueError(f'Суммирование с элементом {other} невозможно.\n'
                             f'Аргумент должен быть числом или объектом класса {self.__class__.__name__}')


if __name__ == '__main__':
    print(' Инициализация и отображение объектов '.center(120, '-'))
    v1 = Vector(1, 2, 3, 4, 5)
    v2 = Vector(10, 20, 30)
    v3 = Vector()
    print('Состав векторов:', v1, v2, v3, sep='\n')
    print()

    print(' Создание нового объекта, при прибавлении целочисленного значения ко всем элементам вектора '.center(120, '-'))
    print(f'Прибавление ко всем значениям {repr(v1)} числового значения 10')
    sumVectorV1plus10 = v1 + 10
    print(f'Создан {sumVectorV1plus10}')
    print()

    print(' Создание нового объекта, при позиционном сложение элементов векторов '.center(120, '-'))
    print(f'Сложение значений {repr(v1)} и {repr(v2)}')
    sumVectorV1V2 = v1 + v2
    print(f'Создан {sumVectorV1V2}')
    print()

    print(' Создание нового объекта, при позиционном умножении элементов векторов '.center(120, '-'))
    print(f'Умножение значений {repr(v1)} и {repr(v2)}')
    mulVectorV1V2 = v1 * v2
    print(f'Создан {mulVectorV1V2}')
    print()
