'''Создание нескольких пользовательских матриц и вариативная обработка значений первых двух

'''
from random import randint as rnd

print('Генерация матриц')
n = int(input("Количество матриц для генерации: "))
N = int(input("Укажите количество строк матрицы: "))
M = int(input("Укажите количество столбцов матрицы: "))
A = []
for i in range(n):
    temp_matrix = [[rnd(-99, 99) for j in range(M)] for i in range(N)]
    A.append(temp_matrix)


def print_matrix(matrix):
    '''Функция для печати элементов матриц в табличном виде'''
    for i in matrix:
        for j in i:
            print("%4d" % j, end="")
        print()


print('Печать всех матриц')
for i in A:
    print_matrix(i)
    print()


def val_matrix():
    '''Функция подсчета и печати результата по двум матрицам'''
    matrix1, matrix2, *matrix_all = A
    go = int(input(
        "Какой операцию необходимо произвести с матрицами: 1 - Сложить, 2 - Умножить, 3 - Возвести в степень m1 на m2: "))
    matrix3 = []
    for i, h_val in enumerate(matrix1):
        row = []
        for j, w_val in enumerate(matrix1[i]):
            mat = (matrix1[i][j] + matrix2[i][j] if go == 1 else matrix1[i][j] * matrix2[i][j]) if go < 3 else \
                matrix1[i][j] ** matrix2[i][j]
            row.append(mat)
        matrix3.append(row)
    print_matrix(matrix3)


if __name__ == '__main__':
    val_matrix()
