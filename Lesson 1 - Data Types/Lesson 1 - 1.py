# Вас просят удостовериться, что имена и фамилии людей
# начинаются в паспортах с большой буквы.


def capital_first_letter(strInput):
    if strInput[0].isalpha():
        strInput = strInput[0].upper() + strInput[1:]
    return strInput

print('Your input:')
inputStr = input()

checkSpace = False
if inputStr[len(inputStr) - 1] == ' ':
    inputStr = inputStr[:-1]
    checkSpace = True

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
if checkSpace:
    inputStr += ' '

print(inputStr)
