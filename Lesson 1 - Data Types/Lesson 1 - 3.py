# Напишите программу Python, чтобы получить строку,
# состоящую из первых 2 и последних 2 символов из данной строки.
# Если длина строки меньше 2, верните вместо нее пустую строку.

print("Задание 3: получение из введенной строки слова, состоящего"
      "из двух первых и двух последних символов строки.")

answer = ''
while answer != 'Y' and answer != 'N':
    print("Автоматический режим ('Y') или ручной ввод в цикле ('N')?")
    answer = input()

inputStr = ''
if answer == 'N':
    print("Введите проверяемую строку:")
    inputStr = input()
elif answer == 'Y':
    inputStr = 'w3resource'
    print("Проверяемая строка:")
    print(inputStr)

while inputStr != '***':
    outputStr = ''

    if len(inputStr) >= 2:
        outputStr = inputStr[:2] + inputStr[-2:]

    print("Итог")
    print(outputStr)

    if answer == 'N':
        print("\nВведите проверяемую строку.")
        print("Для завершения наберите ('***').")
        inputStr = input()
    elif answer == 'Y':
        inputStr = '***'
