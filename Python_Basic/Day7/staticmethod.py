# encoding:utf-8

from math import sqrt

class Triangle(object):
    """docstring for ."""
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c


    @staticmethod
    def is_valid(a,b,c):
        return a+b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        r = self.perimeter() / 2
        return sqrt(r * (r - self._a) * (r - self._b) * (r - self._c))


def funmain():
    a,b,c = 3,4,5
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(Triangle.perimeter(t))
        print(t.area())
        print(Triangle.area(t))
    else:
        print('无法构    三角形')


if __name__ == '__main__':
    funmain()
