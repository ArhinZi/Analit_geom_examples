# Задача 3. Квадраты.
# Дан прямоугольник размера   где   - натуральные числа.
# Разработайте программу разбиения этого прямоугольника
# на наименьшее возможное число квадратов.
# Размеры квадратов могут быть различными.


def get_squares(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            n = int(a / b)
            print("N= {0}; Side= {1}".format(n, b))
            a = a % b
        else:
            n = int(b / a)
            print("N= {0}; Side= {1}".format(n, a))
            b = b % a


if __name__ == "__main__":
    print("A= ", end="")
    a = int(input())
    print("B= ", end="")
    b = int(input())
    get_squares(a, b)
    print(a, b)
