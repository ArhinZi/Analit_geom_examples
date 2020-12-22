# Задача
# 2.1.Найти
# число
# m
# нулей, которыми
# заканчивается
# число
# n!  в
# десятичной
# системе
# счисления.


def get_num_div(a: int, d: int):
    s = 0
    degd = d
    while a >= degd:
        s += int(a / degd)
        degd = degd * d
    return s


if __name__ == "__main__":
    print("N= ", end="")
    n = int(input())
    m = get_num_div(n, 5)
    print("M=", m)
