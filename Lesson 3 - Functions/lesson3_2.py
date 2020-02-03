"""Написать функцию, которая принимает  произвольное
количество любых аргументов. Аргументами могут быть вложенные
списки и кортежи, содержащие числа и другие списки и кортежи.

Функция должна вернуть произведение и сумму
 всех ненулевых элементов вложенных чисел.

 При обнаружении циклической ссылки нужно
 сообщить пользователю и вернуть None.	"""

from functools import reduce


def rec_ar(argum, lvl, dictid):
    """Получение списка целых чисел и отлов зацикленности"""

    output = []

    for i in argum:
        if not isinstance(i, int):
            idi = id(i)
            search = dictid.get(idi)
            if search is None:
                dictid.setdefault(idi, lvl)
            elif lvl > search:
                raise Exception("Зациклились")

    for i in argum:
        if isinstance(i, int):
            output.append(i)
        else:
            if lvl == 1:
                output.extend(rec_ar(i, lvl + 1, {id(i): lvl}))
            else:
                output.extend(rec_ar(i, lvl+1, dictid))
    return output


def rec_kw(kwargum):
    """Получение списка целых чисел и отлов зацикленности"""

    output = []
    for i in kwargum:
        if isinstance(i, int):
            output.append(i)
        elif isinstance(i, (list, tuple)):
            output.extend(rec_ar(i, 1, {id(i): 0}))
        elif isinstance(kwargum.get(i), int):
            output.extend(kwargum.get(i))
        else:
            output.extend(rec_kw(kwargum.get(i)))
    return output


def func(*args, **kwargs):
    """Функция принимающая аргументы для работы"""

    lisnnum = rec_ar(args, 1, {id(args): 0})
    lisnnum.extend(rec_kw(kwargs))

    filteredlist = filter(lambda x: x != 0, lisnnum)

    summer = sum(lisnnum)

    multiple = reduce(lambda res, x: res*x, filteredlist, 1)

    print("Список чисел:", lisnnum, '\nСумма:', summer,
          '\nПроизведение:', multiple)

try:
    print("Проверяем функцию вида:")
    print('foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), '
          'b=(3, 4, [5, 6, [7, 8], []]))')

    func(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
except Exception as exep:
    print(exep)

try:
    print("\nПроверяем функцию вида:")
    print('foo(1, 2, [3, 4, (5, 6, 0)], a, b=(3, 4, [5, 6, [7, 8], []]))')
    print("где a = [1, 2, 3]; a.append(a)")

    A = [1, 2, 3]
    A.append(A)
    func(1, 2, [3, 4, (5, 6, 0)], A, b=(3, 4, [5, 6, [7, 8], []]))
except Exception as exep:
    print(exep)

try:
    print("\nПроверяем функцию вида:")
    print('foo(1, 2, [3, 4, (5, 6, 0)], a, b=(3, 4, [5, 6, [7, 8], []]))')
    print("где a = [1, 2, 3, [1, 2, 3]]; a[3].append(a)")
    A = [1, 2, 3, [1, 2, 3]]
    A[3].append(A)
    func(1, 2, [3, 4, (5, 6, 0)], A, b=(3, 4, [5, 6, [7, 8], []]))
except Exception as exep:
    print(exep)

try:
    print("\nПроверяем функцию вида:\n",
          'foo(1, a, [3, 4, (5, a, 0)], a, b=(3, 4, [5, 6, [7, 8], []]))')
    print("где a = [1, 2, 3]")

    A = [1, 2, 3]
    func(1, A, [3, 4, (5, A, 0)], A, b=(3, 4, [5, 6, [7, 8], []]))
except Exception as exep:
    print(exep)

try:
    print("\nКонтрпример, требующий доработки алгоритма:\n",
          'foo(1, 2, [a, 4, (a, 6, 0)], b=(3, 4, [5, 6, [7, 8], []]))')
    print("где a = [1, 2, 3]")

    A = [1, 2, 3]
    func(1, 2, [A, 4, (A, 6, 0)], b=(3, 4, [5, 6, [7, 8], []]))
except Exception as exep:
    print(exep)
