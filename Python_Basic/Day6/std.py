# encoding: utf-8

class Stdudent(object):
    """docstring forstdudent."""
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s 正在学习 %s .' % (self.name,course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s 只能观看《熊出没》.' % self.name)
        else:
            print('%s 可以观看戏剧.' % self.name)

def main():
    s1 = Stdudent('王贺',30)
    s1.study('Python 编程课程')
    s1.watch_movie()

    s2 = Stdudent('毛贺',13)
    s2.study('语文')
    s2.watch_movie()


if __name__ == '__main__':
    main()
