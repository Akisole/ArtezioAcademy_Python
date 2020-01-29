# Написать функцию вычисления факториала числа


def fuctorial(n: int) -> int:
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


def print_fuctorial():
    print("Введите число n для вычисления факториала:")
    n = int(input())
    print("Факториал", n, ":", fuctorial(n))


print_fuctorial()
