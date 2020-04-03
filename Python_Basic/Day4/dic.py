# encoding:utf-8
print('字面量语法方式创建字典')
dicx = {"姓":"姓名","年":"年龄","籍":"籍贯"}
print(dicx)


print('构造器语法创建字典')
dicy = dict(a='name',b='age',c='adr')
print(dicy)


print('推导式语法创建字典')
dic = {num : num ** 2 for num in range(1,10)}
print(dic)

print('zip 函数将两个序列压成字典')
dic0 = dict(zip(['a','b','c'],'123'))
dic1 = dict(zip(['a','b','c','d'],'123'))
print(dic0,dic1)

print('依据键获取对应值')
print(dicx['姓'])
print(dicy['a'])


print('字典遍历')
for key in dicy:
    print(key,dicy[key])

print('更新字典中元素')
dicm = {'米饭':29,'面条':30,'馒头':16}
print(dicm)
dicm['米饭'] = 99
print(dicm)
dicm.update(lengmian=88,mantou=86)
print(dicm)
if '米饭' in dicm:
    print(dicm['米饭'])

print('get0')
print(dicm.get('米饭'))
print('get1')
print(dicm.get('冷面'))
print('get2')
print(dicm.get('冷面',66))

print('****** 字典删除操作 ******')
dicl = {'米饭':29,'面条':30,'馒头':16,'饺子':36,'包子':98}
print(dicl)
print(dicl.popitem())
print(dicl.popitem())
# print(dicl.pop('馒头':16)
print(dicl.clear())
