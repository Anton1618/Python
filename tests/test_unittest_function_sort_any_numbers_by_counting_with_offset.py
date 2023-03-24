from lesson_functions.sort_any_numbers_by_counting_with_offset import number_count
from unittest import TestCase, main

class Sort_Any_Numbers_By_Counting_With_Offset_Test(TestCase):
    def test_quan4_min0_max1(self):
        self.assertEqual(number_count([0, 0, 1, 1]), [(0, 2), (1, 2)])
        self.assertEqual(number_count([0, 0, 0, 1]), [(0, 3), (1, 1)])

    def test_quan10_min10_max10(self):
        self.assertEqual(number_count([-10, -2, 10, 1, -2, 1, -7, 10, 8, -10]), [(-10, 2), (-7, 1), (-2, 2), (1, 2), (8, 1), (10, 2)])
        self.assertEqual(number_count([-10, 10, -10, -10, -10, -10, -10, -10, -10, -10]), [(-10, 9), (10, 1)])

    def test_quan1_000_000_min1_max1(self):
        self.assertEqual(number_count([-1]*1_000_000), [(-1, 1000000)])
        self.assertEqual(number_count([-1]*500_000+[1]*250_000+[0]*250_000), [(-1, 500000), (0, 250000), (1, 250000)])


if __name__ == '__main__':
    main()