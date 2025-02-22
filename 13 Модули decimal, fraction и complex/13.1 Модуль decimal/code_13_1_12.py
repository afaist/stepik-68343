"""
Дополните приведенный код так, чтобы он вывел сумму наибольшей и наименьшей
цифры Decimal числа.
"""

from decimal import Decimal

num = Decimal(input())
num_tuple = num.as_tuple()
digits = list(num_tuple.digits)
if int(num) == 0:
    print(max(digits))
else:
    print(max(digits) + min(digits))
