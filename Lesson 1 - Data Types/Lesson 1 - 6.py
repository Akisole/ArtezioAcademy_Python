# Напишите скрипт Python для создания и печати словаря,
# содержащего число (от 1 до n) в виде (x, x*x).

print('Your N:')
n = int(input())

outputDict = {}

for i in range(1, n+1):
    outputDict[i] = i*i

print(outputDict)
