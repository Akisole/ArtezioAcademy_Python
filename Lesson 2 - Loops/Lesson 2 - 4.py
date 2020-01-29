# Написать свою имплементацию функции range() из Python 2.x
# (аналогично Python 3, только возвращает список).


def my_range(start, end, step=1):
    outputList = []
    i = start
    while i < end:
        outputList.append(i)
        i += step
    return outputList


def print_myrange():
    print("Введите интервал [a, b] и шаг h (через Enter):")
    a = int(input())
    b = int(input())
    h = int(input())
    print("Range:", my_range(a, b, h))


print_myrange()
