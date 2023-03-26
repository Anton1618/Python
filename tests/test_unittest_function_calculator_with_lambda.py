from unittest import TestCase, main
from practice_functions.calculator_with_lambda import calculate

class Calculator_With_Lambda_Test(TestCase):
    def test_plus(self):
        # Для всех тестов применяется распространенный алгоритм red/green.
        # Его суть в том, чтобы сначала создать ложно результирующий тест (red), ложное значение или просто предположение с ответом на результат работы теста
        # Затем установливается истинно результирующий тест (green), например, на основе полученных данных из ответа,
        # включающего строки Actual(указанный результат, например предположение) и Expected(истинно ожидаемый результат)

        # self.assertEqual(calculate('2+2'), 5) # Ложный тест
        self.assertEqual(calculate('2+2'), 4) # Истинный тест

    def test_minus(self):
        self.assertEqual(calculate('5-3'), 2)

    def test_multi(self):
        self.assertEqual(calculate('2*5'), 10)

    def test_devide(self):
        self.assertEqual(calculate('10/2'), 5.0)

    def test_no_signs(self): # Тест на отсутствие знака в аргументе
        with self.assertRaises(ValueError) as e:
            calculate('abracadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self): # Тест на присутствие нескольких знаков
        with self.assertRaises(ValueError) as e:
            calculate('2+2+2')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])

    def test_many_signs(self): # Тест на присутствие множества знаков
        with self.assertRaises(ValueError) as e:
            calculate('2+2*10')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])

    def test_no_ints(self): # Тест на применение не целых значений
        with self.assertRaises(ValueError) as e:
            calculate('2.2+1.0')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])

    def test_strings(self): # Тест на применение строк вместо числовых значений
        with self.assertRaises(ValueError) as e:
            calculate('a+b')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])

    def test_zero_division(self): # Тест на деление на ноль
        with self.assertRaises(ZeroDivisionError) as e:
            calculate('10/0')
        self.assertEqual('Нельзя делить на ноль', e.exception.args[0])


# Внедрение автоматического вызова через построение конфигурации:
# Edit Configuration -> символ + для добавления новой конфигурации -> Python Tests -> Unittest ->
# перевод конфигурации в режим "castom".
# Настройка его аргументов: discover -s tests -p '*_test.py' # Включение в поиск тестов всех файлов с названием, включающим _test.py
if __name__ == '__main__':
    main()
