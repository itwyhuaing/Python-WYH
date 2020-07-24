# encoding:utf-8

# 继承

class Person(object):
    def __init__(self, name,age):
        self._name = name
        self._age  = age

    @property
    def name(self):
        return self._name

    @property
    def age(slef):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        print('%s 正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s 正在观看话剧 ' % self._name)
        else:
            print('%s 只能观看《熊出没》' % self._name)

class Student(Person):
    def __init__(self, name,age,grade):
        super(Student,self).__init__(name,age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade

    def study(self,course):
        print('%s 年级的 %s 正在学习 %s .' % self._grade,self._name,course)


def fmain():
    print('fmain')
    # p = Person('刘彻',29)
    # p.play()
    s = Student('刘彻',29,'6')
    s.play()
    s.watch_av()
    # s.study('地理')
    s.age = 9
    s.watch_av()


if __name__ == '__main__':
    fmain()
