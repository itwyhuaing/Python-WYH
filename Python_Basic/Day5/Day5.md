### 常用函数


```
# 区间 [start, stop) 上 步进step 的整数，默认步进为 1.
range(start, stop, step)

# [a,b) 区间内随机整数
random.randint(a,b)

# [a,b) 区间步进为s的随机整数
random.randrange(a, b, s)


# 随机浮点数
random.random()
random.uniform(a, b)

# 随机字符
random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')

# 多个字符中生成指定数量的随机字符
random.sample('zyxwvutsrqponmlkjihgfedcba',5)

# 随机选取字符串：
random.choice(['剪刀', '石头', '布'])

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)

# 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
str.join(sequence)
'-'.join("a","b","c") // a-b-c

# 排序规则，reverse = True 降序， reverse = False 升序（默认）；函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。该方法没有返回值，但是会对列表的对象进行排序。
sort(key=None, reverse=False)

# 从序列a中随机抽取 n 个元素，并将n个元素生以list形式返回。
sample(序列a，n)

```
