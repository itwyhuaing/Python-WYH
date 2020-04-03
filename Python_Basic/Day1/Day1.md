### Python 了解

* Python 是解释型语言，具有平台的可移植性；同时支持面向对象编程和函数式编程；Python 中可以调用C/C++代码，展示了其很好的可扩展性和可嵌入性。

### Python 开发环境配置 (以下没有特别说明，均为macOS系统)

* macOS 自带 Python 2.x 版本。Linux或macOS系统的终端中键入下面的命令：

```
Python3 --version
```

* 终端输入python或python3进入交互式环境，即可进入python开发；也可以用文本编辑工具编写python代码之后，保存为.py文件。

* 运行 .py 文件代码。

```
cd (xxx.py文件所在目录)
python xxx.py  或    python3 xxx.py

```

* 单行注释 - 以#和空格开头的部分；多行注释 - 三个引号开头，三个引号结尾。


### 数据类型与变量

* 常见数据类型有：整型（int）、浮点数、字符串、复数。

* 变量命名： 数字、字母、下划线构成；数字不能开头；大小写字母敏感；不要与关键字和系统保留字冲突。

* 在Python中可以使用type函数对变量的类型进行检查。

```
a = 321
c = 1+3j
d = 12.12
f = "Hello,world"
h = True

print(type(a)) # <type 'int'>
print(type(c)) # <type 'complex'>
print(type(d)) # <type 'float'>
print(type(f)) # <type 'str'>
print(type(h)) # <type 'bool'>

```

* 可以使用Python中内置的函数对变量类型进行转换。

```
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。

```

* 运算符及其优先级。
