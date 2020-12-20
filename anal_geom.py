from field_rat import Rat, sqr
import math


class Point:
    u: Rat
    v: Rat

    def __str__(self):
        return "{0};{1}".format(self.u, self.v)


def swap_points(a: Point, b: Point):
    a, b = b, a


def ord_4_points(a1: Point, a2: Point, a3: Point, a4: Point):
    print("==Before Ord==")
    print("A= {0}".format(a1))
    print("B= {0}".format(a2))
    print("C= {0}".format(a3))
    print("D= {0}".format(a4))

    if a1.u > a2.u:
        swap_points(a1, a2)
    if a2.u > a3.u:
        swap_points(a2, a3)
    if a3.u > a4.u:
        swap_points(a3, a4)

    if a1.u > a2.u:
        swap_points(a1, a2)
    if a2.u > a3.u:
        swap_points(a2, a3)

    if a1.u > a2.u:
        swap_points(a1, a2)

    print("==After Ord==")
    print("A= {0}".format(a1))
    print("B= {0}".format(a2))
    print("C= {0}".format(a3))
    print("D= {0}".format(a4))


class IntPoint:
    u: int
    v: int

    def __str__(self):
        return "{0};{1}".format(self.u, self.v)


class Circle:
    x: int
    y: int
    r: int

    def __str__(self):
        return "({0} {1} {2}".format(self.x, self.y, self.r)


def solve_rat_sys(a11: Rat, a12: Rat, b1: Rat, a21: Rat, a22: Rat, b2: Rat, p: Point):
    det = a11 * a22 - a12 * a21
    detX = b1 * a22 - b2 * a12
    detY = a11 * b2 - a21 * b1
    print("Det= {0}".format(det))
    p.u = detX / det
    p.v = detY / det


def line_via_2_points(a: Point, b: Point, a1: Rat, a2: Rat, f: Rat):
    a2 = b.u - a.u
    a1 = a.v - b.v
    f = a.v * a2 + a.u * a1


def intersect_lines(a: Point, b: Point, c: Point, d: Point, p: Point):
    print("=======")
    print("A= {0}".format(a))
    print("B= {0}".format(b))
    print("C= {0}".format(c))
    print("D= {0}".format(d))

    a11: Rat
    a12: Rat
    b1: Rat
    a21: Rat
    a22: Rat
    b2: Rat
    line_via_2_points(a, b, a11, a12, b1)
    line_via_2_points(c, d, a21, a22, b2)
    solve_rat_sys(a11, a12, b1, a21, a22, b2, p)


# Вычисляет позицию точки P(под, на, над) относительно прямой через 2 точки AB
def point_rel_line(a: Point, b: Point, p: Point):
    Au = a.u.num / a.u.den
    Av = a.v.num / a.v.den
    Bu = b.u.num / b.u.den
    Bv = b.v.num / b.v.den
    Pu = p.u.num / p.u.den
    Pv = p.v.num / p.v.den

    x1 = Bu - Au
    y1 = Bv - Av
    x2 = Pu - Au
    y2 = Pv - Av

    r_loc = x1 * y2 - x2 * y1

    if r_loc < 0:
        return -1
    elif r_loc == 0:
        return 0
    else:
        return 1


# Проверяет, что Точки В и С лежат по разные стороны от отрезка АД
def points_rel_line(a: Point, b: Point, c: Point, d: Point):
    return point_rel_line(a, d, b) * point_rel_line(a, d, c) == -1


# Проверяет лежит ли Точка Р(u; v) лежит внутри круга С(x, y, R)
def point_in_circle(p: Point, c: Circle):
    x = Rat.int2rat(c.x)
    y = Rat.int2rat(c.y)
    r = Rat.int2rat(c.r)

    d = sqr(x - p.u) + sqr(y - p.v)
    return d <= sqr(r)


# Проверяет входит ли круг С0 входит в круг С1
def involve(c0: Circle, c1: Circle):
    return (c1.r >= c0.r) and ((math.sqrt(c1.x - c0.x) + math.sqrt(c1.y - c0.y)) <= math.sqrt(c1.r - c0.r))


# Проверяет пересекаются ли круги С0 и С1
def intersect_2_circles(c0: Circle, c1: Circle):
    return (math.sqrt(c1.x - c0.x) + math.sqrt(c1.y - c0.y)) <= math.sqrt(c1.r + c0.r)


# Процедура вычисляет точку пересечения 3-х хорд С1 и С2, С1 и С3, С2 и С3
def get_main_point(c1: Circle, c2: Circle, c3: Circle, p: Point):
    a11 = Rat.int2rat(2 * (-c2.x + c1.x))
    a12 = Rat.int2rat(2 * (-c2.y + c1.y))
    a21 = Rat.int2rat(2 * (-c3.x + c1.x))
    a22 = Rat.int2rat(2 * (-c3.y + c1.y))

    d1 = math.sqrt(c1.r) - math.sqrt(c1.x) - math.sqrt(c1.y)
    d2 = math.sqrt(c2.r) - math.sqrt(c2.x) - math.sqrt(c2.y)
    d3 = math.sqrt(c3.r) - math.sqrt(c3.x) - math.sqrt(c3.y)

    b1 = Rat.int2rat(int(d2 - d1))
    b2 = Rat.int2rat(int(d3 - d1))

    solve_rat_sys(a11, a12, b1, a21, a22, b2, p)
    print("P= {0}".format(p))


# Процедура вычисляет среднюю точку хорды перечечения 2-х окружностей
def get_middle_point(d1: Circle, d2: Circle, pmid: Point):
    a1 = d1.x
    b1 = d1.y
    r1 = d1.r
    a2 = d2.x
    b2 = d2.y
    r2 = d2.r

    a = -2 * a2 + 2 * a1
    a_2 = a * a
    b = -2 * b2 + 2 * b1
    b_2 = b * b
    c = (r2 * r2 - a2 * a2 - b2 * b2) - (r1 * r1 - a1 * a1 - b1 * b1)

    u = a_2 + b_2
    vx = -(2 * b_2 * a1 + 2 * c * a + 2 * a * b * b1)
    vy = -(2 * a_2 * b1 + 2 * c * b + 2 * b * a * a1)

    pmid.u = Rat(-vx, 2 * u)
    pmid.v = Rat(-vy, 2 * u)


#  Проверяет лежит ли точка внутри треугольника
def point_in_triangle(a: Point, b: Point, c: Point, p: Point):
    res1 = point_rel_line(a, b, p)
    res2 = point_rel_line(b, c, p)
    res3 = point_rel_line(c, a, p)
    return (res1 == res2) and (res2 == res3)
