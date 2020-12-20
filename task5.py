# Задача 5. Лист бумаги
# Лист клетчатой бумаги шириной A  и высотой B  разрезали
# на несколько полос горизонтальными разрезами по линиям бумаги.
# Потом каждую из полос разрезали, в свою очередь, на несколько
# прямоугольников вертикальными разрезами по линиям бумаги.
# Один из полученных прямоугольников удалили, а остальные
# перенумеровали от 1  до N  и измерили их ширину Xi  и высоту Yi,
# i = 1,2,...,N. Ориентацию прямоугольников относительно листа
# бумаги при этом не меняли (см. рис. 3). Написать программу поиска
# размеров - ширины W  и высоты H удаленного прямоугольника.


def input_array(u, v, n: int):
    for i in range(n):
        print("U[{0}], V[{1}]= ".format(i, i), end="")
        inp = input().split()
        u.append(int(inp[0]))
        v.append(int(inp[1]))


def getWH(x, y, n: int):
    s = 0
    for i in range(n):
        s += x[i] * y[i]
    return s


def getW(x, a: int, n: int):
    l = 0
    for i in range(n):
        l += x[i]
    return a - l % a


if __name__ == "__main__":
    print("A= ", end="")
    a = int(input())
    print("B= ", end="")
    b = int(input())
    print("N= ", end="")
    n = int(input())
    X = []
    Y = []
    input_array(X, Y, n)
    WH = a * b - getWH(X, Y, n)
    W = getW(X, a, n)
    H = int(WH / W)
    print("W= {0}".format(W))
    print("H= {0}".format(H))
