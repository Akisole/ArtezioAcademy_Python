# Напишите скрипт Python для объединения двух словарей Python
# Значения второго словаря имеют приоритет


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

print("Задание 7: объединение двух словарей. "
      "Значения второго словаря имеют приоритет  ")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

dict1 = {}
dict2 = {}
inputStr = ''
while inputStr != '***':
    if answer == 'N':
        print('Введите пары ключ значение для Первого словаря '
              '(разделяя их через Enter).')
        print("Для завершения набора введите ('***')")
        dict1 = get_dict()
        print('Введите пары ключ значение для Второго словаря '
              '(разделяя их через Enter).')
        print("Для завершения набора введите ('***')")
        dict2 = get_dict()

    elif answer == 'Y':
        dict1 = {'cow': 1, 'pig': 5, 'cat': 1, 'dog': 2}
        dict2 = {'cat': 3, 'goat': 4, 'pig': 5}
        inputStr = '***'

    print("Словари:\n", dict1, '\n', dict2)

    dict1.update(dict2)

    print("Объединение:\n", dict1)

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите что-то другое")
        inputStr = input()
