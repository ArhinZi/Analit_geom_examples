# Задача  6.1 Обыкновенные дроби
# Написать программу, которая переводит обыкновенную дробь
# в десятичную периодическую дробь
# A,B(C). p, q – натуральные числа в интервале [1; 10000],
# записанные в десятичной системе счисления.


def ordinal2periodic(p: int, q: int):
    d = []
    r = []

    a = int(p / q)
    p = int(p / q)

    p = 10 * p

    j = 0
    p = 10 * p
    d.append(int(p / q))
    r.append(p % q)
    while True:
        j += 1
        p = 10 * p
        d.append(int(p / q))
        r.append(p % q)
        i = 0
        while d[i] != d[j]:
            i += 1

        if i < j:
            break

    b = 0
    for ki in range(i):
        b = b * 10 + d[ki]

    c = 0
    for ki in range(j):
        c = c * 10 + d[ki]

    return a, b, c


if __name__ == "__main__":
    print("P= ", end="")
    p = int(input())
    print("Q= ", end="")
    q = int(input())
    a, b, c = ordinal2periodic(p, q)
    print("A= {0}".format(a))
    print("B= {0}".format(b))
    print("C= {0}".format(c))
