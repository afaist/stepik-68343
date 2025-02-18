"""
    Генератор паролей 2

Напишите программу, которая с помощью модуля random генерирует nn паролей
длиной mm символов, состоящих из строчных и прописных английских букв и цифр,
кроме тех, которые легко перепутать между собой:

    «l» (L маленькое);
    «I» (i большое);
    «1» (цифра);
    «o» и «O» (маленькая и большая буквы);
    «0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя
бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа n и m, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести n паролей длиной m символов в соответствии с условием
задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли
сгенерировать возможно.

Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна
цифра и буква в верхнем и нижнем регистре.

Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:

    функция generate_password(length) – возвращает случайный пароль длиной
    length символов;
    функция generate_passwords(count, length) – возвращает список, состоящий из
    count случайных паролей длиной length символов.

Примечание 4. Приведенные ниже тесты – это лишь образцы возможного ответа.
Возможны и другие способы генерации паролей.
"""

import random
from string import ascii_uppercase, ascii_lowercase

LETTER_UPPER = "".join(set(ascii_uppercase) - set("IO"))
LETTER_LOWER = "".join(set(ascii_lowercase) - set("lo"))
LETTER_DIGITS = "23456789"


def generate_password(length: int) -> str:
    password = []
    choice = ["upper", "lower", "digit"]
    for _ in range(length):
        letter = random.choice(choice)
        symbol = ""
        if letter == "upper":
            choice.remove("upper")
            symbol = random.choice(LETTER_UPPER)
        elif letter == "lower":
            choice.remove("lower")
            symbol = random.choice(LETTER_LOWER)
        elif letter == "digit":
            choice.remove("digit")
            symbol = random.choice(LETTER_DIGITS)
        password += symbol
        if len(choice) == 0:
            choice = ["upper", "lower", "digit"]
    random.shuffle(password)
    return "".join(password)


def generate_passwords(count: int, length: int) -> list[str]:
    return [generate_password(length) for _ in range(count)]


print(*generate_passwords(int(input()), int(input())), sep="\n")
