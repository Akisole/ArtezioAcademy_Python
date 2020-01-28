# Вам дается 3 набора, найдите, является ли
# третий набор подмножеством первого и второго наборов


def get_set():
    inputList = []
    cycle = input()

    while cycle != '***':
        inputList.append(cycle)
        cycle = input()

    return inputList

print("Задание 5: определение того, является ли "
      "третий набор подмноджеством первого и второго наборов.")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

inputStr = ''
set1 = ''
set2 = ''
set3 = ''
while inputStr != '***':
    if answer == 'N':
        print('Введите первый набор (через Enter)')
        print("Чтобы завершить - наберите ('***')")
        set1 = set(get_set())
        print('Введите второй набор (через Enter)')
        print("Чтобы завершить - наберите ('***')")
        set2 = set(get_set())
        print('Введите третий набор (через Enter)')
        print("Чтобы завершить - наберите ('***')")
        set3 = set(get_set())
    elif answer == 'Y':
        set1 = {1, 2}
        set2 = {2, 3}
        set3 = {2}
        inputStr = '***'

    print("Проверка над множествами:\n", set1, "\n", set2, "\n", set3)

    outSet = set3.issubset(set1 | set2)

    print("Итог: ", outSet)

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите что-то другое")
        inputStr = input()
