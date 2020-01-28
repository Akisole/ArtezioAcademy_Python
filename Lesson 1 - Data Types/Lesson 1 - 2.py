# Напишите программу Python для подсчета количества символов
# (частоты символов) в строке.

print("Задание 2: подсчет частоты каждого символа в введенной строке.")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

inputList = []
if answer == 'N':
    print("Введите проверяемую строку:")
    inputList = list(input())
elif answer == 'Y':
    print("Проверяемая строка:")
    print('google.com')
    inputList = list('google.com')

inputStr = ''
while inputStr != '***':
    outputDict = {}
    while len(inputList):
        popLetter = inputList.pop()
        if outputDict.get(popLetter) is None:
            outputDict[popLetter] = 1
        else:
            outputDict[popLetter] += 1

    print("Итог")
    print(outputDict)

    if answer == 'N':
        print("\nВведите проверяемую строку.")
        print("Для завершения наберите ('***').")
        inputStr = input()
        inputList = list(inputStr)
    elif answer == 'Y':
        inputStr = '***'
