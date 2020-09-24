# li = [1, 2, 3, 4, 5]
# li.append(6)  # [1,2,3,4,5,6]
# li.insert(2, 2.5)  # [1,2,2.5,3,4,5,6]
# li.insert(100, 100)  # [1,2,2.5,3,4,5,6,100]
# li.insert(-100, 0)  # [0,1,2,2.5,3,4,5,6,100]
# li.extend([102, 102, 103, 104])  # [0, 1, 2, 2.5, 3, 4, 5, 6, 100, 102, 102, 103, 104]
# print(li)
# print(li.pop())  # 2.5


li_1 = [1, 2, 3, 1, 1, 1, 12, 12, 2, 1, 2, 2, 1, 112, 21, 1, 1]
# 用成员运算符删除同一个数
# while 1 in li_1:
#     li_1.remove(1)
# print(li_1)

# 用for循环
# li2 = [1, 2, 3, 1, 1, 1, 12, 12, 2, 1, 2, 2, 1, 112, 21, 1, 1]
# 现将li2切片
# li3 = li2[::]
# for x in li3:
#     if x == 1:
#         li2.remove(x)
# print(li2)

# 也可以写成这样,用一个新的空列表将除了1以外的数字粘贴,那么返回一个新的列表
# li4 = []
# for x in li2:
#     if x != 1:
#         li4.append(x)
# print(li4)


# sort排序 从小到大
# l2 = [2, 23, 1, 25, 53, 456, 457, 234, 2]
# l2.sort()
# print(l2)

# 从大到小
l2 = [2,23,1,25,53,456,457,234,2]
l2.sort(reverse=True)
print(l2)

lst = list(range(1,11))
lst_2 =[]
for x in lst:
    lst_2.append(x**2)
print(lst_2)