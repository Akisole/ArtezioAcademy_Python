# Напишите программу на Python, чтобы найти
# самые высокие 3 значения в словаре.
# Вывод: только значения.


def get_dict():
    outputDict = {}
    cycle = input()
    while cycle != '***':
        cycle2 = input()
        if cycle2 != '***':
            outputDict[cycle] = cycle2
        else:
            break
        cycle = input()
    return outputDict


print("Задание 8: нахождение трех максимальных значения в словаре.")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()


dict1 = {}
inputStr = ''
while inputStr != '***':
    if answer == 'N':
        print('Введите пары ключ значение(int) для словаря '
              '(разделяя их через Enter).')
        print("Для завершения набора введите ('***')")
        dict1 = get_dict()
    elif answer == 'Y':
        dict1 = {'cow': 1, 'pig': 5, 'cat': 2, 'dog': 2}
        inputStr = '***'

    print("Словарь:\n", dict1)

    valuesList = list(dict1.values())
    valuesList.sort()

    print('Самые большие 3 значения:\n', valuesList[-3:])

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите что-то другое")
        inputStr = input()
