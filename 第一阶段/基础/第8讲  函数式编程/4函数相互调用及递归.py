# def f1():
#     print('f1')
#
#
# def f2():
#     f1()
#     print("f2")
#
# f2()




# 递归
# def print_num(num):
#     if num == 0:
#         return    # 结束函数
#     print(num)
#     num -= 1
#     print_num(num)
#     print("*************")
#
# print_num(3)


"""
# 1 1 2 3 5 8 13 21 34 55....
# 给定数字n
n = 3
    a = 1 b = 1 1+1=2
n=4
    print(a+b)
    a,b = b,a+b

"""


# n = 40
# # 非递归方式
# a = 1   # n-2项
# b = 1   # n-1项
# for i in range(1,n+1):
#     if i == 1 or i ==2:
#         print(1)
#     else:
#         print(a+b)
#         a,b = b,a+b



def fib(n):
    """求第n项的数"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(10))
import time
s= time.time()
print(fib(50))
e = time.time()
print(e-s)
