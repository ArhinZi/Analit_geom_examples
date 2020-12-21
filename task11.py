# Задача 1.1. Младшие цифры степени.
# Разработать программу, которая по натуральным числам   ищет число   ,
# равное двум младшим цифрам степени  . Учесть, что число   может
# выйти за границы целого типа.
import math


def quick_mod_pow(a: int, n: int, d: int):
    r: int
    if n > 0:
        r = int(math.sqrt(quick_mod_pow(a, int(n / 2), d)) % d)
        if n % 2 == 1:
            r = (r * a) % d
    else:
        r = 1
    return r


if __name__ == "__main__":
    print("A= ", end="")
    a = int(input())
    print("N= ", end="")
    n = int(input())

    m = quick_mod_pow(a, n, 100)
    print("M=", m)
