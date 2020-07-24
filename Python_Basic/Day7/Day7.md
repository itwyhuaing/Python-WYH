### 面向对象编程 - 2

* property 装饰器

```
外部可修改 age 属性

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

```

* Python是一门动态语言。通常动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。

```
__slots__ 实际应用可见 slots.py 文件

```

* 类之间的关系有三种：is-a（继承或泛化）、has-a（关联）和use-a（依赖）关系。
