# encoding:utf-8

print('********* 单个数组操作 *********')
l1 = [1,3,5,7,9,11,100]
print(l1)

l2 = l1 * 3
print(l2)

l3 = ['test'] * 3
print(l3)



# 计算列表长度(元素个数) 7
print(len(l1))
# 下标取值 1，100
print(l1[0])
print(l1[-1])
# 下标获取指定内容 [3, 5]    [1, 3, 5, 7]
print(l1[1:3])
print(l1[:4])
# [7,9] []
print(l1[-4:-2])
print(l1[-4:2])
# [3,7,11]    [1,5,9,100]
print(l1[1::2])
print(l1[::2])
# [7,3]  [7,11]
print(l1[-4::-2])
print(l1[-4::2])
# [7,11]  [7,3]
print(l1[3::2])
print(l1[3::-2])

# 遍历
for ele in l1:
    print('遍历获取元素：%d' % ele)

for index in range(len(l1)):
    print('遍历下标：%d - %d ' % (index,l1[index]))

for index , ele in enumerate(l1):
    print('enumerate 遍历 %d - %d ' % (index,ele))

print('********* 数组间操作 *********')
l1.append(200)
print(l1)
l1.insert(1,11)
print(l1)
l1.extend([22,33])
print(l1)
l1+=[55,66]
print(l1)


l1.remove(22)
print(l1)
l1.remove(l1[0])
print(l1)
l1.remove(l1[len(l1)-1])
print(l1)
l1.pop(0)
print(l1)
l1.pop(len(l1) - 1)
print(l1)
# python 3.* 版本可执行
# l1.clear()
# print(l1)


print('********* 数组排序操作 *********')
sl1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
sl2 = sorted(sl1)
print(sl2)

sl3 = sorted(sl1,reverse=True)
print(sl3)

sl4 = sorted(sl1,key=len)
print(sl4)

# sl5 = sort(reverse=True)
# print(sl5)



print('********* 生成式和生成器 *********')
import sys
f = [x for x in range(1, 10)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

# 生成式
f = [x ** 2 for x in range(1,10)]
print(f)
print(sys.getsizeof(f))

# 生成器对象
f = (x ** 2 for x in range(1,10))
print(f)
print(sys.getsizeof(f))

for val in f:
    print('遍历生成器所生成的列表元素 %d ' % val)
