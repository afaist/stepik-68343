"""
    Симметричная матрица

Напишите программу, которая проверяет симметричность квадратной матрицы
относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в
матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной
диагонали, или NO в противном случае.
"""

n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            print("NO")
            exit(0)
print("YES")
