"""
    Операции над комплексными числами

Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их
сумму, разность и произведение.

Формат входных данных
На вход программе подаются два комплексных числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести ответ на задачу.
"""

z1 = complex(input())
z2 = complex(input())
print(f"{z1} + {z2} = {z1 + z2}")
print(f"{z1} - {z2} = {z1 - z2}")
print(f"{z1} * {z2} = {z1 * z2}")
print(f"{z1} / {z2} = {z1 / z2}")
