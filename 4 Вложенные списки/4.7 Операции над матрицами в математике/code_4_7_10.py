"""
    Умножение матриц 🌶️

Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и
столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка.
Далее следуют числа m и k — количество строк и столбцов второй матрицы затем
элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""

n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]
input()
r, c = [int(x) for x in input().split()]
b = [[int(x) for x in input().split()] for _ in range(r)]
result = [[0] * c for _ in range(n)]
for i in range(n):
    for j in range(c):
        for k in range(r):
            result[i][j] += a[i][k] * b[k][j]
for i in result:
    print(*i)
