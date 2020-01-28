# Напишите программу Python для удаления дубликатов из списка.


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

print("Задание 9: удаление дубликатов из списка "
      "с сохранением порядка. ")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

inputList = []
inputStr = ''
while inputStr != '***':
    if answer == 'N':
        inputList = get_list()
    elif answer == 'Y':
        inputList = ['abc', 'xyz', 'aba', 'abc']
        print("Проверяемый список:")
        print(inputList)
        inputStr = '***'

    inputList.reverse()

    i = 0
    while i != len(inputList) - 1:
        if inputList.count(inputList[i]) > 1:
            inputList.pop(i)
        else:
            i += 1

    inputList.reverse()
    print('Результат удаления дубликатов:')
    print(inputList)

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите что-то другое")
        inputStr = input()
