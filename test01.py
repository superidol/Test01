# -*- coding: utf-8 -*-
# from sympy import *
import sympy as sym  # 引入Sympy 模块
import os

d1 = "Hello Worlds"
print(d1)
d2 = 1
d3 = 4
d4 = (1, 2, 3, 4, ['a', 'b'], 5, '678')
print(d4)
d4[4][0] = 'cd'
d4[4][1] = 'ef'
print(d4[0])
print(len(d4))
print(d4[4])
for aa in d4:  # 遍厉元组中的元素
    print(aa)
    print(())
for i in range(len(d4)):
    print('%s---d4[%s]=%s' % (type(d4[i]), i, d4[i]))

# ds=type(d4[i])
# print(ds)


# 利用sympy 解数学方程
x = sym.Symbol('x')
y = sym.Symbol('y')
print(sym.solve([y + x - 1, 3 * x + 2 * y - 5], [x, y]))
diss = (sym.solve([y + x - 1, 3 * x + 2 * y - 5], [x, y]))
# print (limit(1/x**2, x, 0))
print(diss)
print(type(diss))
print(diss[x], diss[y])  # 结果在Dict中

# 利用字符串 建立对应关系 替换另一个字符
str1 = 'abcd'  # 原始字母
taDB = '人民公社'  # 对应翻译码
# trantab=str.maketrans(str1,taDB)
st = 'abbdaaacd'
print(st.translate(str.maketrans(str1, taDB)))

# 字典的用法
student = {'小萌': '1001', '小智': '1002', '小强': '1003'}
print('小强的学号是：%(小强)s' % student)

x = {}
y = x
x['val'] = 12  #
print(x, y)

st = student.copy()

print(st)
st['小强'] = '4445'
print(student)
print(st)
# 列表中的字典
dirdd = [{'id': 1001, 'imm': 'sttr'}, {'idd': 'p01', 'dis': 123}]
print(len(dirdd))
print(dirdd[0], dirdd[1])
print(dirdd[0]['id'])

dirdd.append({'dsd': 90909})
print(dirdd)

d2 = [1, 2, 3, 4, 5]
print(d2)
d2[2:] = list('7')
print(d2.count(1))

a1 = [1, 2, 3, 4]
b1 = ['a', 'b', 'c', 'd']
c1 = a1.copy()
a1[len(a1):] = b1
print(a1)
c1.extend(b1)  # c1.extend(b1) 和 a1[len(a1):]=b1的结果是一样的，都是用于在列表末尾一次性追加另一个序列中的多个值

print(a1.index("a"))
print(a1.index(1))

xxx = 111
if xxx in a1:
    print('X属于A1')
else:
    print('X不属于A1')

for iii in a1:
    print(iii)

print(len(a1))
isis = 0
# 使用while 循环 读取List的值
while isis < len(a1):
    print('a[%s]=%s' % (isis, a1[isis]))
    isis = isis + 1

'''
多行注释
多行注释
多行注释
'''

dic1 = {'a': (1, 88), 'b': 2, 'c': 3, 'd': 4}  # 字典 同一Key 赋值多个。
print(dic1['a'][0])
print(dic1['a'][1])

dic2 = {('a', 'b'): 100}
print(dic2['a', 'b'])

# 字典中去重复
d = {'d': 0, 'b': 0, 'c': 1, 'a': 0, 'e': 1, 'f': 0, 'h': 2}
func = lambda z: dict([(x, y) for y, x in z.items()])
print(d)
print(func(d))
print(func(func(d)))
d2 = (func(func(d)))
print(d2)

'''  Python中list、dict去重 
# 1. 清晰明了版（不改变顺序）：
ids = [1,2,3,3,4,2,3,4,5,6,1]
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)
print (news_ids)

# 2.  简介快速版
# 利用set的自动去重功能：

li=[1,2,3,4,5,1,2,3]
li=list(set(li))
print(li)
# 这样处理会改变list原有顺序，若想保持顺序不变，则如下：

li=[1,2,3,4,5,1,2,3]
new_li=list(set(li))
new_li.sort(key=li.index)
print(new_li)

# 3. 匿名函数版
ids = [1,4,3,3,4,2,3,4,5,6,1]
func = lambda x,y:x if y in x else x + [y]
reduce(func, [[], ] + ids)
# 4. 高级模块版 
import itertools
ids = [1,4,3,3,4,2,3,4,5,6,1]
ids.sort()
it = itertools.groupby(ids)sql
for k, g in it:
    print (k)
# 5. 数量级GB左右文本快速去重
#coding=utf-8 
import sys, re, os
def quchong(infile, outfile):
    inopen = open(infile, 'r', encoding='utf-8')
    outopen = open(outfile, 'w', encoding='utf-8')
    data = inopen.read()
    list_1 = list(set(data.split('\n')))
    print(list_1)
    for line in list_1:
        if line != '':
            outopen.write(line + '\n')
    inopen.close()
    outopen.close()
# 6. 字典针对Value去重：
# 由于字典要求“键”必须不一致，因此可通过将键值对调换位置进行去重，完成后再换回去即可。

func = lambda z: dict([(x, y) for y, x in z.items()])     # 字典键值对位置互换
result = func(func(tw))
'''
