# Задача 1.3. Старшие цифры степени
# Разработать программу, которая ищет наименьшее
#  число N  вида 2^k*5^m,  начинающееся с цифр 999
import math


def get_pow(d: int):
    i = 0
    lg = 0
    lgd = math.log(d) / math.log(10)
    lg999 = math.log(9.99) / math.log(10)
    while True:
        i += 1
        lg += lgd
        lg10 = lg - int(lg)
        if lg10 > lg999:
            break
    return i, lg


if __name__ == "__main__":
    k, lg2 = get_pow(2)
    print("k=", k)
    print("Lg2=", lg2)
    m, lg5 = get_pow(5)
    print("m=", m)
    print("Lg5=", lg5)
    if lg2 < lg5:
        d = 2
        n = k
    else:
        d = 5
        n = m
    print("N=", d, "^", n)
