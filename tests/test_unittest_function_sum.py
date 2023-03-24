from unittest import TestCase, main

class Summ_test(TestCase):
    def test_lst_num(self):
        self.assertEqual(sum([1, 2, 3]), 6)
        self.assertEqual(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)


if __name__ == "__main__":
    main()