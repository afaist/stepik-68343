"""
Список по образцу 1

На вход программе подается число n. Напишите программу, которая создает и выводит построчно список, состоящий из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный список.
"""

n = int(input())
print(*[[i + 1 for i in range(n)] for _ in range(n)], sep="\n")
