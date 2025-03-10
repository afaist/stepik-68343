"""
    Сумма дробей 1

На вход программе подается натуральное число nn. Напишите программу, которая
вычисляет и выводит рациональное число, равное значению выражения:
сумма обратных квадратов чисел от 1 до n.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание 1. Результирующая дробь должна быть несократимой.

Примечание 2. Подробнее о ряде обратных квадратов можно почитать по ссылке.
"""

from fractions import Fraction

n = int(input())
result = 0
for i in range(1, n + 1):
    result += Fraction(1, i**2)
print(result)
