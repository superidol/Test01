# 1. 列表的常用操作（增，删，改，查）
list1 = [0, 1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]
list3 = ["a", "b", "c"]
list4 = [4, 56, 7, 89, 99, 123, 3]
list1.append(100)  # 将指定值添加到列表的尾部
print(list1)

list1.insert(4, 88)  # 指定位置插入指定值
print(list1)

list1.pop(3)  # 删除指定位置的元素
print(list1)

list1.pop()  # 删除最后一个元素
print(list1)

list3.clear()  # 清空列表
print(list3)

list1.remove(1)  # 删除指定值
print(list1)

list1[3] = "abc"  # 修改指定位置的元素
print(list1)

a = list1.index(2)  # 用于从列表中找出某个值第一个匹配项的索引位置
print(a)

list1.extend(list2)  # 将一个列表list2添加到列表list1的尾部
print(list1)

b = len(list2)  # 计算列表长度的算法
print("b = %d" % b)

a = [45, 5, 2, 78, 90]  # 对列表a排序
print(sorted(a))
b = [3, 6, 2, 0]
print(b.sort())  # 对列表a排序

# 2. 元组的常用操作方法
# tuple元组和列表类似，不同的地方是元组元素不能修改(重点)
tuple1 = (12, 34, 45)
print(type(tuple1))  # 查看数据类型

for a in tuple1:  # 遍历元组
    print(a, end=" ")

if 34 in tuple1:  # 判段元组中是否有某元素
    print("存在该元素")
else:
    print("不存在该元素")

tuple2 = (23, 5, 9, 6)
a = tuple2.count(9)  # 统计某元素出现的次数
b = tuple2.index(5)  # 获取指定元素的小标
c = len(tuple2)  # 获取元组的长度
print(a)
print(b)
print(c)

# 3. 字典的常用操作
dict1 = {"name": "张三", "addr": "北京顺义区", "age": 12}
dict1.pop("addr")  # 删除字典中的元素
print(dict1)  # 结果：{'name': '张三', 'age': 12}

for i in dict1:  # 字典的遍历，这种情况默认遍历到的是键名
    print(i)

for a in dict1.keys():  # 和上一种方法结果一样
    print(a)

for b in dict1.values():  # 得到值
    print(b)

for c in dict1.items():  # 得到键值对，以元组的形式输出
    print(c)

for k, v in dict1.items():  # 遍历键名和键值
    print(k, v)
