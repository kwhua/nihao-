# 需求定义一个函数，给定一个数字，遍历从1到该数字之间的所有数字
def func(n):
    """遍历从1到该数字之间的所有数字"""
    for i in range(1,n+1):
        print(i,end=" ")

# 调用
# func(10)
# func(100)


# 需求定义一个函数，给定两个数字，遍历两个数字之间的所有数字(包含边界)
def func2(m,n):
    """遍历从m到n之间的所有数字"""
    for i in range(m,n+1):
        print(i,end=" ")


func2(10,100)
