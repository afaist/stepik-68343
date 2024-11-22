"""
    Магический квадрат 🌶️

Магическим квадратом порядка n называется квадратная таблица размера n×n,
составленная из всех чисел 1,2,3,…,n^2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равны между собой. Напишите
программу, которая проверяет, является ли заданная квадратная матрица
магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в
матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые
пробелами.

Формат выходных данных
Программа должна вывести YES, если матрица является магическим квадратом, или
NO в противном случае.
"""

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# получаем множество чисел матрицы
numbers = set(sum(matrix, []))
if len(numbers) != n**2 or min(numbers) != 1 or max(numbers) != n**2:
    print("NO")
    exit(0)
# Транспонируем матрицу
trans_matrix = [list(row) for row in zip(*matrix)]
summa = sum(matrix[0])
summa_d1 = 0
summa_d2 = 0
for i in range(n):
    if sum(matrix[i]) != summa or sum(trans_matrix[i]) != summa:
        print("NO")
        exit(0)
    summa_d1 += matrix[i][i]
    summa_d2 += matrix[i][n - i - 1]
if summa_d1 != summa or summa_d2 != summa:
    print("NO")
    exit(0)
print("YES")
