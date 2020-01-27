# Напишите программу Python для подсчета количества строк,
# где длина строки равна 2 или более, а первый и последний символ
# одинаковы из заданного списка строк.


def get_list():
    print('Print your list.\n(To Exit type ***)')

    inputList = []
    cycle = input()

    while cycle != '***':
        inputList.append(cycle)
        cycle = input()

    print('Your list:')
    print(inputList)

    return inputList


def check_task4(inputStr):
    if len(inputStr) >= 2:
        if inputStr[0] == inputStr[len(inputStr)-1]:
            return True
    else:
        return False


inputList = get_list()

outputNum = 0
for i in inputList:
    if check_task4(i):
        outputNum += 1

print('Answer: ', outputNum)
