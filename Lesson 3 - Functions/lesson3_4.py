""" На вход функции передается строка с xml документом
 (тэги без аттрибутов, корневой элемент только один).
 Нужно выполнить следующее преобразование
 и вывести максимальную вложенность."""

import xml.etree.ElementTree as ET

CURRDEPTH = -1
MAXDEPTH = 0


def get_children(link):
    """Нахождение всех потомков звена"""

    childlist = []

    global CURRDEPTH
    global MAXDEPTH
    CURRDEPTH += 1
    if MAXDEPTH < CURRDEPTH:
        MAXDEPTH = CURRDEPTH

    if len(link) != 0:
        childlink = list(link)
        for child in childlink:
            childdict = {N: child.tag}
            grandchildlist = get_children(child)
            childdict.setdefault(CH, grandchildlist)
            childlist.append(childdict)

    CURRDEPTH -= 1
    return childlist


A = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
N = 'name'
CH = 'children'

TREE = ET.fromstringlist(A)
DICTTREE = {N: TREE.tag, CH: get_children(TREE)}

print("a: '", A, "'")
print(DICTTREE, ",", MAXDEPTH)
