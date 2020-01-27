# Напишите программу Python для подсчета количества символов
# (частоты символов) в строке.

print('Your string:')
inputList = list(input())
outputDict = {}

while len(inputList):
    popLetter = inputList.pop()
    if outputDict.get(popLetter) is None:
        outputDict[popLetter] = 1
    else:
        outputDict[popLetter] += 1

print(outputDict)
