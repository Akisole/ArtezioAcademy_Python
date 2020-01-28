# Напишите программу на Python,
# чтобы получить разницу между двумя списками


def get_list():
    print("Введите строки по одной (через Enter).")
    print("Чтобы завершить - наберите ('***')")

    inputList = []
    cycle = input()

    while cycle != '***':
        inputList.append(cycle)
        cycle = input()

    print('Введенный список:')
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

print("Задание 10: разница между двумя списками. ")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

inputList1 = []
inputList2 = []
inputStr = ''
while inputStr != '***':
    if answer == 'N':
        inputList1 = get_list()
        inputList1 = get_list()
        inputList1 = del_dupl_list(inputList1)
        inputList2 = del_dupl_list(inputList2)
    elif answer == 'Y':
        inputList1 = ['abc', 'xyz', 'aba']
        inputList2 = ['aba', 'dfg', 'sd', 'abc']
        print("Проверяемые списки:")
        print(inputList1)
        print(inputList2)
        inputStr = '***'

    outputList = []

    for i in inputList1:
        if inputList2.count(i) == 0:
            outputList.append(i)

    for i in inputList2:
        if inputList1.count(i) == 0:
            outputList.append(i)

    print("Разница между списками:")
    print(outputList)

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите что-то другое")
        inputStr = input()
