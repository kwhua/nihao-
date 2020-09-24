lst = list(range(1, 11))
# 将lst中的每个元素平方后放入新列表中
lst_2 = [x * x for x in lst]
print(lst_2)
# 将lst中的奇数放入新列表中
lst_3 = [x for x in lst if x % 2 == 1 if x == 3]
print(lst_3)

# 练习将一个嵌套列表转换为一维列表
lst_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst_4 = [y for x in lst_1 if type(x) == list for y in x ]
# print(lst_4)
# lst_5 = [lst_1[x][y] for x in range(0,len(lst_1)) for y in range(x+1) ]
# print(lst_5)
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for x in t1:
    print(x)
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
t2 = (10, 11, 12, 13)
t3 = t1 + t2
print(t3)

# t1 = ()
# t1[0] = 1
# t1[1] = 2
# t1[2] = 3
# print(t1)

print("-" * 50)
for x in list(range(100)):
    print(x)

t3 = (1, 2, 3, 4, [5, 6, 7, 8, 9])
t3[4].append(t3[4] * 2)
print(t3)
t = ('苹果', '梨', '橘子', '香蕉', '葡萄')
for x, name in enumerate(t, start=1):
    print(f"编号{x}的水果是:{name}")

print(type(name))

for x in enumerate(t, start=1):
    print(x)
print(type(x))

lst3 = lst.copy()
# lst[10].append([11,12])
lst[0] = 2
print(lst3)
print(id(lst[0]))

# 倒序
# 使用切片的方法
a = [1, 4, 56, 8, 2, 42, 75, 4, 79, 34, 34, 21, 3, 6, 344, 3]
x = a[::-1]
print(x)

# 通过 reverse
a.reverse()
print(a)

# 排序 sort() ,默认是按Unicode的顺序进行从小到大排序
a.sort()
print(a)

# 从大到小
a.sort(reverse=True)
print(a)

# 查找
# 已知索引查找元素 list[index]
print(a[3])

print("-" * 50)
# 已知元素查找索引,返回的是满足条件的第一个索引的值 index[]
a = [1, 4, 56, 8, 2, 42, 75, 4, 79, 34, 34, 21, 3, 6, 344, 3]
print(a.index(75))
print("-" * 50)
# count 统计元素在列表中出现的个数,不在将返回0
print(a.count(3))

# 深浅拷贝
import copy

a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print('a', a)  # [1,2, 3, 4, ['a', 'b','c'],5]
print('b', b)  # [1,2, 3, 4, ['a', 'b','c'],5]
print('c', c)  # 1,2, 3, 4, ['a', 'b','c']]
print('d', d)  # 1,2, 3, 4, ['a', 'b']]

# 推导式
lst = list(range(1, 11))
print(lst)
# 不使用推导式  将 奇数的平方输出
lst1 = []
for x in range(1, 11):
    if x % 2 == 1:
        lst1.append(x ** 2)
print(lst1)
# 使用推导式
lst2 = [x * x for x in range(1, 11) if x % 2 == 1]
print(lst2)

for x in range(1, 11):
    if x > 6:
        print(x)
    else:
        print(x * x)

lst4 = [x if x > 6 else x * x for x in range(1, 11) ]
print(lst4)
