""" Написать функцию, которая будет принимать только
    4 позиционных аргументы (все аргументы числовые).
    Функция должна вернуть среднее арифметическое аргументов и
    самый большой аргумент за все время вызовов функции"""


def get_list_int(string):
    """Input: string like "1 2 32 1"
      Output: list like [1, 2, 32, 1]"""

    instr = string
    finder = []

    while instr[len(instr)-1] == ' ':
        instr = instr[:-1]

    space = instr.find(' ')
    while space != -1:
        finder.append(int(instr[:space+1]))
        instr = instr[space+1:]
        space = instr.find(' ')
    finder.append(int(instr))

    return finder


def arithmetic_average_and_max():
    """calculates the arithmetic mean and outputs
       the maximum argument for all time"""

    maxel = ''

    def inner(list_in):
        value = sum(list_in) / 4

        nonlocal maxel
        if maxel == '':
            maxel = max(list_in)
        else:
            list_in.append(maxel)
            maxel = max(list_in)
            list_in.pop()

        return print("Аргументы:", list_in, "\nCреднее арифметическое:", value,
                     "\nМаксимальный аргумент за все время", maxel, '\n')

    return inner


ANSWERTASK = arithmetic_average_and_max()
while True:
    print("Введите четыре аргумента (например, '1 2 3 4')")
    NUMBERS = get_list_int(input())
    ANSWERTASK(NUMBERS)
