# encoding:utf-8

print('****************** 集合创建 ******************')
# 创建集合的字面量语法
s1 = {1,2,3,5,6,8,0}
print(s1)
print('length = ',len(s1))

s2 = set(range(1,10))
s3 = set((11,2,23,55,66,88,99,0))
print(s2)
print(s3)

# 创建集合的推导式语法(推导式也可以用于推导集合)
s4 = {num for num in range(1, 30) if num % 3 == 0 or num % 5 == 0}
print(s4)


print('****************** 集合中元素的添加与删除 ******************')
s5 = {22,33,55,66,88,00}
print(s5)
s5.add(1)
print(s5)
s5.add('wy')
print(s5)
s5.update([90,91])
print(s5)
s5.discard(96)
print(s5)

if 00 in s5:
    s5.remove(00)
print(s5)

print('pop : %d ' % s5.pop())
print(s5)

s6 = {'v','r','y'}
s7 = {'q','a','z'}
s8 = (s6,s7)
print(s8)

print('****************** 集合的成员、交集、并集、差集等运算 ******************')
s01 = {1,2,3,4,5,6,8}
s02 = {1,3,5,7,9}

print('intersection')
print(s01 & s02)
print(s01.intersection(s02))

print('union')
print(s01 | s02)
print(s01.union(s02))

print('difference')
print(s01 - s02)
print(s01.difference(s02))

print('symmetric_difference')
print(s01 ^ s02)
print(s01.symmetric_difference(s02))

print('***判断子集和超集***')
print('issubset issuperset')
print(s01 <= s02)
print(s01.issubset(s02))
print(s02.issuperset(s01))
