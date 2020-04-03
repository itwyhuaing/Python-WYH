# encoding: utf-8


# usr = raw_input('please n :')
# pw  = raw_input('please pw:')
#
# if usr == 'admin' and pw == '668866':
#     print("OK")
# else:
#     print("NO")
#
#
# score = int(input('please input :'))
# if score >= 85:
#     if score == 100:
#         print('满分')
#     else :
#         print('A')
# elif score > 60:
#     print("C")
# else :
#     print("D")


# sum = 0
# for x in range(101):
#     print(" x = %d " % x)
#     sum += x
# print("计算结果：%d" % sum)

# import random
# tmp = True
# while tmp:
#     x = random.randint(1,16)
#     print('x = %d' % x)
#     tmp = not (x % 10 == 0)



row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
