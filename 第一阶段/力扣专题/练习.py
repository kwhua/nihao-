lst = [1,5,3,5,2,1]
def func(lst):

    # 将列表装换为集合,用变量s接收
    s =set(lst)
    # 再将集合转换为列表 用lst2接收
    lst2 = list(s)
    print(lst2)

# 调用func函数
func(lst)