"""
    Заполнение диагоналями 🌶️

На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m, заполнив её "диагоналями" в соответствии
с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m —
количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3
символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно
обойтись и без ljust(), система примет и такое решение 😇
"""

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
value = 1
# d - число диагоналей
for d in range(m + n - 1):
    for i in range(d + 1):
        # идем по диагонали
        if i < n and (d - i) < m:
            matrix[i][d - i] = value
            value += 1
# вывод матрицы
for row in matrix:
    print(*[str(i).ljust(2) for i in row])
