# Напишите программу Python, чтобы получить строку,
# состоящую из первых 2 и последних 2 символов из данной строки.
# Если длина строки меньше 2, верните вместо нее пустую строку.

print('Your string:')
inputStr = input()
outputStr = ''

if len(inputStr) >= 2:
    outputStr = inputStr[:2] + inputStr[-2:]

print(outputStr)
