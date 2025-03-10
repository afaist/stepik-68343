"""
    Онлайн-школа BEEGEEK 6 🐝🌶️

Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников
присутствовал на всех уроках с начала учебного года. Для каждого урока есть
листок со списком присутствовавших учеников.

Напишите программу, определяющую фамилии учеников, которые присутствовали на
всех уроках.

Формат входных данных
На вход программе в первой строке подается число m – количество уроков,
проведенных с начала учебного года. Далее идет mm блоков строк, описывающих
листки с фамилиями. На первой строке каждого блока указано количество фамилий
ni, затем идет ni строчек с фамилиями тех, кто был на i-ом
уроке.

Формат выходных данных
Программа должна вывести фамилии учеников, которые были на всех уроках,
отсортированных в лексикографическом порядке. Каждая фамилия должна быть
записана на отдельной строке.

Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.
"""

lessons = int(input())
names = {input() for _ in range(int(input()))}
for i in range(lessons - 1):
    n = int(input())
    names = names & {input() for _ in range(n)}
print(*sorted(names), sep="\n")
