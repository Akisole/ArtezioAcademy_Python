# Напишите программу Python для удаления дубликатов из списка.
# Без сохранения порядка


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

output = list(set(inputList))
print('Answer:\n', output)
