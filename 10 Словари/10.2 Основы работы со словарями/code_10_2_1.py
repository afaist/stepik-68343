"""
Сравнение занимаемого места в ОЗУ между: множестом, frozenset, списокм,
кортежом и словарем.
Сравнение времени прохода по всей коллекции каждого типа.
"""

from time import time
from sys import getsizeof

# В count хранится правая граница range для коллекций.
COUNT = 40_000


def size_info(array):
    """
    Получение кол-во занимаемой памяти в ОЗУ разными типами коллекций.
    """
    print(
        f"  Память {(str(type(array).__name__)).ljust(10, ' ')} = {round(getsizeof(array) / 1024 / 1024, 3)} Мб"
    )


def create_array(array):
    """
    Создаем разные типаы коллекций в интервале от 1 до COUNT.
    """
    match array:
        case "set":
            array = set(range(1, COUNT + 1))

        case "frozenset":
            array = frozenset(range(1, COUNT + 1))

        case "list":
            array = list(range(1, COUNT + 1))

        case "tuple":
            array = tuple(range(1, COUNT + 1))

        case "dict":
            array = {num: num for num in range(1, COUNT + 1)}

    size_info(array)
    return array


def cycle_array(array):
    for i in range(COUNT):
        if i in array:
            pass


def time_info(array):
    """
    Замеряем время прохождение по всей коллекции.
    """
    time_start = time()

    cycle_array(array)

    print(
        f"  Время {(str(type(array).__name__)).ljust(12, ' ')}: {time() - time_start} сек."
    )

    if type(array).__name__ in {"list", "set"}:
        array.clear()


def start():
    """
    Сравниваем множества, списки и кортежи
    """
    print(f"[В колелекциях содержится по {COUNT:_} элементов]", end="\n\n")
    print("Проверяем занимаемую память:", end="\n")
    my_set = create_array("set")
    my_frozenset = create_array("frozenset")
    my_list = create_array("list")
    my_tuple = create_array("tuple")
    my_dict = create_array("dict")

    print("\nПроверяем затраченное время на прохождение по всей коллекции:")
    time_info(my_set)
    time_info(my_frozenset)
    time_info(my_list)
    time_info(my_tuple)
    time_info(my_dict)
    print()


if __name__ == "__main__":
    start()
