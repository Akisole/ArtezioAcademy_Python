# Напишите программу на Python,
# чтобы получить разницу между двумя списками


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


def del_dupl_list(inputList):
    inputList.reverse()

    i = 0
    while i != len(inputList) - 1:
        if inputList.count(inputList[i]) > 1:
            inputList.pop(i)
        else:
            i += 1

    inputList.reverse()

    return inputList


inputList1 = get_list()
inputList2 = get_list()

inputList1 = del_dupl_list(inputList1)
inputList2 = del_dupl_list(inputList2)
# листы без дубликатов

outputList = []

for i in inputList1:
    if inputList2.count(i) == 0:
        outputList.append(i)

for i in inputList2:
    if inputList1.count(i) == 0:
        outputList.append(i)

print('Answer:\n', outputList)
