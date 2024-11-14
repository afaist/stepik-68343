"""
Создание и вывод матриц
"""

print("Создание и вывод матриц")


def print_matrix(matrix: list):
    rows = len(matrix)
    columns = len(matrix[0])
    print(f"Матрица {rows}x{columns}:")
    print("=" * columns * 6)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(6), end="")
        print()
    print("=" * columns * 6)


matrix = [[277, -930, 11, 0], [9, 43, 6, 87], [4456, 8, 290, 7]]

print_matrix(matrix)
print()
print("Создаем нулевую квадратную матрицу")
n = 8
matrix = [[0] * n for _ in range(n)]
print_matrix(matrix)
print("Заполненяем главную диагональ едининицами, а побочную двойками")
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 2
print_matrix(matrix)
"""
Индексы i и j элементов на главной диагонали связаны соотношением i = j. Индексы i и j элементов на побочной диагонали связаны соотношением i + j + 1 = n (или  j = n - i - 1), где n — размерность матрицы.

Заметим также, что:

    если элемент находится выше главной диагонали, то i < j, если ниже - i > j.
    если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже - i + j + 1 > n.

"""
