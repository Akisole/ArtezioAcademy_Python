""" Написать несколько функций, которые в качестве единственного
    аргумента принимают список (или кортеж) целых чисел.
    первая функция должна вернуть квадраты элементов коллекции;
    вторая функция должна вернуть только элементы на четных позициях;
    третья функция возвращает кубы четных элементов на нечетных позициях."""


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


def func1(list_in):
    """returns the squares of the list items"""
    answer = []

    for i in list_in:
        answer.append(int(i)*int(i))

    return answer


def func2(list_in):
    """returns elements in even positions in the input_list"""
    answer = []

    size = len(list_in)
    for i in range(size):
        if (i+1) % 2 == 0:
            answer.append(list_in[i])

    return answer


def func3(list_in):
    """returns cubes of even elements at odd positions in the list"""
    answer = []

    size = len(list_in)
    for i in range(size):
        if (i + 1) % 2 != 0:
            if list_in[i] % 2 == 0:
                answer.append(list_in[i]*list_in[i]*list_in[i])

    return answer


TESTLIST1 = [-2, 2, 4, 3, 5]
print('Input your list (for example "1 2 3 4 5"): ')
TESTLIST2 = get_list_int(input())

print('Your list:', TESTLIST2)
print('Func1:', func1(TESTLIST2))
print('Func2:', func2(TESTLIST2))
print('Func3:', func3(TESTLIST2))

print('Test list:', TESTLIST1)
print('Func1:', func1(TESTLIST1))
print('Func2:', func2(TESTLIST1))
print('Func3:', func3(TESTLIST1))
