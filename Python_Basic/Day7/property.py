# encoding:utf-8

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age  = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age >= 30 and self._age < 56:
            print('哄孩子')
        elif self._age <= 10:
            print('念小学')
        else:
            print('休闲')



def fmain():
    p = Person('孙悟空',8)
    p.play()
    p.age = 36
    p.play()
    p.age = 66
    p.play()


if __name__ == '__main__':
    fmain()
