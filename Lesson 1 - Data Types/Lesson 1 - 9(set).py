# Напишите программу Python для удаления дубликатов из списка.
# Без сохранения порядка


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
      "без сохранения порядка. ")

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

    output = list(set(inputList))
    print('Результат удаления дубликатов:')
    print(output)

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите что-то другое")
        inputStr = input()
