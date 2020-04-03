# encoding:utf-8
from math import sqrt

class Point(object):
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def  move_to(self,x,y):
        self.x = x
        self.y = y

    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy

    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x),str(self.y))




def funmain():
    p1 = Point(1,1)
    print(p1)
    p2 = Point()
    print(p2)
    p2.move_by(-2,-2)
    print(p2)
    p2.move_to(-1,-1)
    print(p2)
    print(p1.distance_to(p2))




if __name__ == '__main__':
    funmain()
