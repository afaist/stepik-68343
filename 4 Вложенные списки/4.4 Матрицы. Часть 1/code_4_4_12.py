"""
Максимальный в области 1

Напишите программу, которая выводит максимальный элемент в заштрихованной
области квадратной матрицы (ниже главной диагонали).

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в
матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной
области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
"""

n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
maximum = matrix[0][0]
for i in range(n):
    for j in range(n):
        if j <= i and matrix[i][j] > maximum:
            maximum = matrix[i][j]
print(maximum)
