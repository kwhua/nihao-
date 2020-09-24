# map
lst = [1, 2, 3]
# 将lst转化为[1,4,9]
# 推导式
lst1 = [x ** 2 for x in lst]

print("-" * 50)


def func1(x):
    return x ** 2


lst2 = map(func1, lst)  # lst2中的内容要遍历才能读取出来

for x in lst2:
    print(x)
# 遍历完以后指针指向最后面,在转换为列表就为空
lst4 = list(lst2)
print(lst4)  # []
# 只要内置函数处理可迭代对象时,才会造成这种现象,常用的不会
# 如果我们需要一直用到转换的对象时,直接使用,不要赋值
# for x in map(func,lst)
# print(map(func,lst))

for x in lst:
    print(x)
lst3 = list(lst)
print(lst3)

#
# 练习过滤出列表的所有奇数
lst5 = list(range(1, 11))
# 推导式
lst6 = [x for x in range(1, 11)]


# 定义函数
def f2(n):
    if n % 2 == 1:
        return True
    else:
        return False


print(filter(f2, lst5))

for x in filter(f2, lst5):
    print(x)

print("-" * 50)
# zip
# 练习现在有两个元组('a','b'),('c','d'),
l1 = []
d1 = dict()
for x in zip(('a', 'b'), ('c', 'd')):
    d1[x[0]] = x[1]
    l1.append(d1)
print(dict(d1))
# for y in x:
#     d1[x][]=y


print(list(zip({'a', 'b'}, {'c', 'd'})))

func3 = lambda x, y: x if x > y else y
print(func3(21, 32))


print("-"*50)
def f():
    li = []
    for i in range(5):
        li.append(lambda x:i**x)
    return li
li = f()
print(li[0](3))
print(li[1](3))
print(li[2](3))
print(li[3](3))
print(li[4](3))


def f():
    li = []
    for i in range(5):
        # li.append(lambda x,y=i:y**x)
        def li(x,y=i):
            print(y**x)
    return li
li = f()
li(3)
li(3)
li(3)
li(3)
li(3)
# print(li[0](3))
# print(li[1](3))
# print(li[2](3))
# print(li[3](3))
# print(li[4](3))


print("-"*50)
def f():
    li = []
    for i in range(5):
        # li.append(lambda x:i**x)
        def f2(x,y=i):
            print( y**x)
        li.append(f2)
    return li


li = f()
li[0](3)
li[1](3)
li[2](3)
li[3](3)
li[4](3)






