a = 3
b = 2
c = 1+3j
d = 12.12
f = "Hello,world"
h = True

print(a+b)
print(a-b)
print(a * b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(f))
print(type(h))


print('%d + %d = %d' % (a, b, a + b))


f = float(input('Please input :'))
c = (f - 32)/1.8
print('%f hsd = %f ssd' % (f,c))


year    = int(input('please input :'))
is_leap = (year % 4  == 0 and year % 100 != 0) or \
          (year % 400 == 0)
print(is_leap)
