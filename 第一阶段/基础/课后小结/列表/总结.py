# 1. 序列操作

# 索引 就是序列

# 切片
lst = [1,2,3,4,5,7,8,9]
# lst[start,stop,step]

# 拼接和重复

# 赋值

# 遍历

# 2. 特有方法
# 增加
    # append(item) 追加在尾部
    # insert(pos,item) 指定添加
    # extend(可迭代对象)  追加在尾部
li = [1,2,3,4,5]
li.append(6)  # [1,2,3,4,5,6]
li.insert(2,2.5)  # [1,2,2.5,3,4,5,6]
li.insert(100,100)  # [1,2,2.5,3,4,5,6,100]
li.insert(-100,0)  # [0,1,2,2.5,3,4,5,6,100]
li.extend([7,8,9])  # [1,2,2.5,3,4,5,6,100,7,8,9]

# 删除
    # pop()  已知索引删元素,默认是最后一个
    # remove(item)  删除第一个满足元素,没有会报错
    # del 待删除的元素
    # clear()  只剩一个空列表
li.pop(2)  # 2.5
l2 = [1,2,3,2,1,321,1,24,22,4]
del l2[3]  # 删除一个元素
del l2[2:5]  # 删除多个元素
del l2  # 删除变量l2,那么l2什么都没有了(包括值,地址等等)
l2.clear()  #  []

# 修改
    # 列表名[index] = new_value
li[2] = "三"
    # reverse() 列表倒序
# 切片倒序
l1 = [1,2,3,4,5,6]
l2 = l1[::-1]
print(l2)
# reverse方法
l1 = [1,2,3,4,5,6]
l1.reverse()
print(l1)
    # sort() 按Unicode编码排序  从小到大sort()  从大到小 sort(reverse = True)

