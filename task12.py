# Задача 1.2. Остаток степени.
# Разработать программу, которая по натуральным числам   и
# ищет остаток от деления степени   на  . Учесть, что число
# может выйти за границы целого типа.


def period(a: int, d: int):
    p = []
    i = 0
    p.append(a % d)
    print(p[i])
    while True:
        i += 1
        p.append((p[i - 1] * a) % d)
        print(p[i], ' ')

        j = 0
        while p[j] != p[i]:
            j += 1
        if j < i:
            break

    ln = i - j
    first = j
    return [ln, first, p]


if __name__ == "__main__":
    print("A= ", end="")
    a = int(input())
    print("N= ", end="")
    n = int(input())
    print("D= ", end="")
    d = int(input())

    ln, first, p = period(a, d)
    print("Len=", ln)
    print("First=", first)

    ind = (n - first) % ln - 1
    res = p[ind]
    print("Res=", res)
    print("OK")
   