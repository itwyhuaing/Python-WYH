# encoding: utf-8

# 找出所有的水仙花数
# for num in range(100,1000):
#     print(num)
#     low = num % 10
#     mid = num // 10 % 10
#     hig = num // 100
#     if num == low ** 3 + mid ** 3 + hig ** 3:
#        print('水仙花数:%d' % num)


# 正整数反转
# num = int(input('请输入随机正整数：'))
# r_num= 0
# while num > 0 :
#     r_num = r_num * 10 + num % 10
#     num //= 10
# print(r_num)


# 百钱百鸡
# for x in range(0,20):
#     for y in range(0,33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z/3 == 100:
#             print('%d 只公鸡 , %d 母鸡 , %d 小鸡' % (x,y,z))


from random import randint

money = 1000
while money > 0:
    print('你的总资产为: %d' % money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')
