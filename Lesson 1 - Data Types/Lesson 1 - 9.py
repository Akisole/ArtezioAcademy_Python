# Напишите программу Python для удаления дубликатов из списка.


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

inputList = get_list()

inputList.reverse()

i = 0
while i != len(inputList) - 1:
    if inputList.count(inputList[i]) > 1:
        inputList.pop(i)
    else:
        i += 1

inputList.reverse()
print('Answer:\n', inputList)
