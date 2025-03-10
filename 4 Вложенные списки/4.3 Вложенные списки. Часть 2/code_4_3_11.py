"""
Tреугольник Паскаля 2 🌶️
На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n  (n≥1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на
отдельной строке в соответствии с образцом.
"""

from math import comb


def print_pascal(row: int):
    for i in range(row):
        print(*[comb(i, k) for k in range(i + 1)])


n = int(input())
print_pascal(n)
