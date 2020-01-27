# Вам дается 3 набора, найдите, является ли
# третий набор подмножеством первого и второго наборов


def get_set():
    inputList = []
    cycle = input()

    while cycle != '***':
        inputList.append(cycle)
        cycle = input()

    return inputList


print('Print first set.\n(To Exit type ***)')
set1 = set(get_set())
print('Print second set.\n(To Exit type ***)')
set2 = set(get_set())
print('Print third set.\n(To Exit type ***)')
set3 = set(get_set())

print("Your set's:\n", set1, "\n", set2, "\n", set3)

outSet = set3.issubset(set1 | set2)

print(outSet)

# if outSet:
#     print("Answer: Subset")
# else:
#     print("Answer: Not a subset")
