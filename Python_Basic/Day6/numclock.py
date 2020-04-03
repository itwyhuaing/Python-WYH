# encoding:utf-8
from time import sleep
class Clock(object):
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s


    def run(self):
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.m += 1
            if self.m == 60:
                self.m = 0
                self.h += 1
                if self.h == 24:
                    self.h = 0

    def show(self):
        return '%02d : %02d : %02d' % (self.h,self.m,self.s)



def funmain():
    clock = Clock(23,59,56)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    funmain()
