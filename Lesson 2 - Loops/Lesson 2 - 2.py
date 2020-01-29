# Написать функцию, которая принимает 3 числа (a,b,c) и
# проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’


def count_number_interval_devide():
    print("Введите три числа (через Enter), где первые два - "
          "границы интервала [a, b], третье - делитель c:")
    a = int(input())
    b = int(input())
    c = int(input())

    count = 0
    for i in range(a, b + 1):
        if i % c == 0:
            count += 1

    print("Чисел, делящихся на", c, ":\n", count)


count_number_interval_devide()
