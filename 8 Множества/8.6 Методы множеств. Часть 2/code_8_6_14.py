"""
Общие числа

На вход программе подаются две строки текста, содержащие числа. Напишите
программу, которая выводит все числа в порядке возрастания, которые есть как в
первой строке, так и во второй.

Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные
символом пробела.

Формат выходных данных
Программа должна вывести на одной строке через пробел числа, встречающиеся в
обеих строках.
"""

first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
print(*sorted(first.intersection(second)))
