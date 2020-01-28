# Вас просят удостовериться, что имена и фамилии людей
# начинаются в паспортах с большой буквы.


def capital_first_letter(strInput):
    if len(strInput) > 0 and strInput[0].isalpha():
        strInput = strInput[0].upper() + strInput[1:]
    return strInput

print("Задание 1: любое слово в строке с заглавной буквы.")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

inputStr = ''
if answer == 'N':
    print("Введите проверяемую строку:")
    inputStr = input()
elif answer == 'Y':
    inputStr = 'swa Sa 1rd adddf'
    print("Проверяемая строка:")
    print(inputStr)

while inputStr != '***':

    listStr = []
    findStr = inputStr

    space = findStr.find(' ')
    while space != -1:
        listStr.append(capital_first_letter(findStr[:space + 1]))
        findStr = findStr[space + 1:]
        space = findStr.find(' ')
    listStr.append(capital_first_letter(findStr))

    inputStr = ''
    for i in listStr:
        inputStr += i

    print("Итог")
    print(inputStr)

    if answer == 'N':
        print("\nВведите проверяемую строку.")
        print("Для завершения наберите ('***').")
        inputStr = input()
    elif answer == 'Y':
        inputStr = '***'
