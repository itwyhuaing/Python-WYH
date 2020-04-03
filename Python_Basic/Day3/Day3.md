### 函数

* 在Python中可以使用def关键字来定义函数，命名规则跟变量的命名规则是一致的。

```
# 参数有默认值
def add(a=1, b=0):
    """三个数相加"""
    return 2*a + b

# 参数无默认值
def add(a, b):
    """三个数相加"""
    return 2*a + b

# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
```


### 模块

* Python中每个文件就代表了一个模块（module），不同的模块中可以有同名的函数。在使用不同模块的同名函数时可以通过 “from module1 import func” 的方式。

```
from module1 import fun_sum
print(fun_sum(1,1))

from module2 import fun_sum
print(fun_sum(1,1))

```


```

import module1 as m1
import module2 as m2

print(m1.fun_sum(1,1))
print(m2.fun_sum(1,1))


```



























6
