# Напишите программу Python для подсчета количества строк,
# где длина строки равна 2 или более, а первый и последний символ
# одинаковы из заданного списка строк.


def get_list():
    print("Введите строки по одной (через Enter).")
    print("Чтобы завершить - наберите ('***')")

    inputList = []
    cycle = input()

    while cycle != '***':
        inputList.append(cycle)
        cycle = input()

    print('Введенные строки:')
    print(inputList)

    return inputList


def check_task4(inputStr):
    if len(inputStr) >= 2:
        if inputStr[0] == inputStr[len(inputStr)-1]:
            return True
    else:
        return False


print("Задание 4: подсчет срок длинной более 2 символов и с совпадением"
      " первого и последнего символа.")

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
        inputList = ['abc', 'xyz', 'aba', '1221']
        print("Проверяемые строки:")
        print(inputList)
        inputStr = '***'

    outputNum = 0
    for i in inputList:
        if check_task4(i):
            outputNum += 1

    print("Число строк, удовлетворяющих условию: ", outputNum)

    if answer == 'N':
        print("\nДля выхода с программы наберите('***').")
        print("Для продолжение - введите что-то другое")
        inputStr = input()
