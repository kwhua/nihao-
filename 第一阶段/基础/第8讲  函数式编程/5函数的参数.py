a = 100
#
# def func(n):
#     print(n)    # 不输出 /100
#     n = 20   # 赋值
#     print(n)  # 20
#
#
# func(a)
# print(a)  # 100


def f(n=[]):
    n.append(3)  # 修改
    n = [1,2,3]   # 赋值：改变引用

    print(f"n的值是{n}")


f()   # n的值是[3]
f()   # n的值是[3,3]


f([10])  #


