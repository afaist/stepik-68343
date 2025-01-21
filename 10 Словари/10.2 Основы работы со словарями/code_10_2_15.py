"""
    Набор сообщений 📩

На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью
цифровой клавиатуры. Поскольку с каждой клавишей связано несколько букв, для
большинства букв требуется несколько нажатий клавиш. При однократном нажатии
цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры
2,3,4 или 5 раз генерирует второй, третий, четвертый или пятый символ
клавиши.
1 	.,?!:
2 	ABC
3 	DEF
4 	GHI
5 	JKL
6 	MNO
7 	PQRS
8 	TUV
9 	WXYZ
0 	space (пробел)

Напишите программу, которая отображает нажатия клавиш, необходимые для
введенного сообщения.

Формат входных данных
На вход программе подается одна строка – текстовое сообщение.

Формат выходных данных
Программа должна вывести нажатия клавиш, необходимых для введенного сообщения.

Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные
буквы.

Примечание 2. Ваша программа должна игнорировать любые символы, не указанные в
приведенной выше таблице.
"""

keys = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " ",
}
new_keys = {}
for key, value in keys.items():
    for n, c in enumerate(value):
        new_keys[c] = key * (n + 1)
message = input().upper()
result = ""
for c in message:
    result += new_keys.get(c, "")
print(result)
