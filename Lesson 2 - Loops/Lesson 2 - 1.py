# Написать функцию, которая печатает квадраты всех
# нечетных чисел в произвольном интервале [0, Х].
# А так же количество таких чисел.


def odd_number_interval(x: int) -> list:
    outputList = []
    for i in range(0, x+1):
        if i % 2 != 0:
            outputList.append(i)
    return outputList


def print_double_oddNumber_innterval():
    print("Введите конец интервала [0, X]: ")
    x = int(input())

    oddNum = odd_number_interval(x)

    outStr = ''
    for i in oddNum:
        outStr = outStr + str(i*i) + ' '

    print("Квадраты чисел: ", outStr, '\nКолличество:', len(oddNum))


print_double_oddNumber_innterval()
