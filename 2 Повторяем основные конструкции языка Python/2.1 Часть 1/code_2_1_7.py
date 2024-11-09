"""
Переворот числа

Дано пятизначное или шестизначное натуральное число. Напишите программу,
которая изменит порядок его последних пяти цифр на обратный.

Формат входных данных
На вход программе подается одно натуральное пятизначное или шестизначное число.

Формат выходных данных
Программа должна вывести число, которое получится в результате разворота,
указанного в условии задачи. Число нужно выводить без незначащих нулей.
"""

number = input()
if len(number) == 5:
    print(int(number[::-1]))
else:
    print(f"{number[0]}{number[1:][::-1]}")
