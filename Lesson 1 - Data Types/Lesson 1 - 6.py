# Напишите скрипт Python для создания и печати словаря,
# содержащего число (от 1 до n) в виде (x, x*x).

print("Задание 6: создание и печать словоря из чисел 1-n  "
      "в виде (x, x*x).")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

inputStr = ''
n = 5

if answer == 'N':
    print('Введите значение n:')
    inputStr = input()

while inputStr != '***':
    if answer == 'N':
        n = int(inputStr)
    elif answer == 'Y':
        inputStr = '***'
        print("Значение n = ", n)

    outputDict = {}

    for i in range(1, n+1):
        outputDict[i] = i*i

    print("Полученный словарь:")
    print(outputDict)

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите значение n")
        inputStr = input()
