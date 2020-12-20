import math


class Rat:
    num: int = 0
    den: int = 0

    def __init__(self, p: int, q: int):
        if p == 0:
            self.num = 0
            self.den = 1
        else:
            g = math.gcd(abs(p), abs(q))
            self.num = int(p / g)
            self.den = int(q / g)
            if self.den < 0:
                self.num = -self.num
                self.den = -self.den

    def __add__(self, other):
        r_num = self.num * other.den + other.num * self.den
        r_den = self.den * other.den
        return Rat(r_num, r_den)

    def __sub__(self, other):
        r_num = self.num * other.den - other.num * self.den
        r_den = self.den * other.den
        return Rat(r_num, r_den)

    def __neg__(self):
        return Rat((-1) * self.num, (-1) * self.den)

    def __mul__(self, other):
        return Rat(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Rat(self.num * other.den, self.den * other.num)

    @staticmethod
    def int2rat(i: int):
        return Rat(i, 1)

    @staticmethod
    def getZero():
        return Rat(0, 1)

    def __eq__(self, other):
        return (self.num == other.num) and (self.den * other.den)

    def __lt__(self, other):
        return (self.num * other.den) < (other.num * self.den)

    def __gt__(self, other):
        return (self.num * other.den) > (other.num * self.den)

    def __le__(self, other):
        return (self.num * other.den) <= (other.num * self.den)

    def __ge__(self, other):
        return (self.num * other.den) >= (other.num * self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


def sqr(x: Rat):
    return x * x
