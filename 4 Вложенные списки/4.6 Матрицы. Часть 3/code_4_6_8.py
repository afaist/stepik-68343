"""
    Заполнение змейкой 🐍

На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m, заполнив её "змейкой" в соответствии с
образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m —
количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3
символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно
обойтись и без ljust(), система примет и такое решение 😇
"""

n, m = [int(x) for x in input().split()]
# Создаем матрицу и разворачиваем каждую нечетную строку
matrix = [
    [str(j + i * m).ljust(2) for j in range(1, m + 1)][:: (-1) ** i] for i in range(n)
]
for row in matrix:
    print(*row)
