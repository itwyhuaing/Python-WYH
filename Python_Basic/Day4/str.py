# encoding:utf-8


# s1 = 'hello , world!'
# s2 = 'hello , world!'
# s3 = """
# hello,
# world!
# """
# print(s1,s2,s3)


# s1 = '\141\142\143\x61\x62\x63'
# s2 = r'\141\142\143\x61\x62\x63'
# print(s1,s2)


s1 = 'hello ' * 3
print(s1)

s2 = 'world'
s1 += s2
print(s1)

print('ll' in s1)
print('good' not in s1)


thestr = 'abc123456'
#ab
print(thestr[0]+thestr[1])
# ab
print(thestr[0:2])
# b
print(thestr[1:2])
# ab
print(thestr[-9:-7])
# c123456
print(thestr[2:])
# abc123
print(thestr[:-3])

# c36
print(thestr[::3])
# b25
print(thestr[1::3])
# 654321cba
print(thestr[::-1])
# 642ca
print(thestr[::-2])
# 52b
print(thestr[-2::-3])
# 25
print(thestr[-5::3])
# 检查字符串是否由数字构成 False
print(thestr.isdigit())
# 检查字符串是否由字母构成 False
print(thestr.isalpha())
# 检查字符串是否由数字和字母构成 True
print(thestr.isalnum())


cnt = 'HOW are yuo'
# 11
print(len(cnt))
# 获得字符串首字母大写的拷贝 How are yuo
print(cnt.capitalize())
# 获得字符串每个单词首字母大写的拷贝 How Are Yuo
print(cnt.title())
# 获得字符串变大写后的拷贝 HOW ARE YUO
print(cnt.upper())
# 从字符串中查找子串所在位置 5
print(cnt.find('re'))
# 从字符串中查找子串所在位置 -1
print(cnt.find('ou'))
# 从字符串中查找子串所在位置 5
print(cnt.index('re'))
# 与find类似但找不到子串时会引发异常
# print(cnt.index('ou'))

# 检查字符串是否以指定的字符串开头 startswith()

# 检查字符串是否以指定的字符串结尾  endswith()

# 将字符串以指定的宽度居中并在两侧填充指定的字符
# *******************HOW are yuo********************
print(cnt.center(50, '*'))

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
# ***************************************HOW are yuo
print(cnt.rjust(50, '*'))

# 将字符串以指定的宽度靠左放置右侧填充指定的字符
# HOW are yuo***************************************
print(cnt.ljust(50, '*'))



t_s = '   hello , please!   '
# 获得字符串修剪左右两侧空格之后的拷贝    hello , please!
print(t_s.strip())



# 格式化
a,b = 6,8
print('{0} * {1} = {2}'.format(a,b,a * b))
# python 3.* 版本生效
# print(f'{a} * {b} = {a * b}')
