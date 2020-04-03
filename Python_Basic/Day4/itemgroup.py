# encoding:utf-8

t = ('汉字',66,6.89,True)
print(t)

# 取值与遍历的方式类似列表


print('********* 元组与列表相互转化 *********')
# 元组转列表
pe = list(t)
print(pe)

# 列表转元组
x = tuple(pe)
print(x)


import sys

print('列表所占内存空间大小 ：%d' % sys.getsizeof(pe))
print('元组所占内存空间大小 ：%d' % sys.getsizeof(x))
