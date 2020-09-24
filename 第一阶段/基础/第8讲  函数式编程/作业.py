# 标准：
# 1 每日笔记整理
# 2 课堂案例练习
# 3 学员选课系统函数式编程改造
#
# 拓展：
# 1  封装函数，传入整数m、n，生成一个列表，值为m到n之间每个整数值的平方（包含边界）
# 2 List = [-2,1,3,-6],如何实现以绝对值大小从小到大将List中内容排序。
# 3 青蛙一次能跳一个或两个台阶，问：有n个台阶，青蛙跳上去有几种跳法


# 1  封装函数，传入整数m、n，生成一个列表，值为m到n之间每个整数值的平方（包含边界）
'''
def func(m,n):
    # 传入整数m、n，生成一个列表，值为m到n之间每个整数值的平方（包含边界）

    lst = []
    for x in range(m,n+1):
        lst.append(x**2)
    print(lst)

num1 = int(input("请输入一个整数:\n"))
num2 = int(input("请输入一个整数:\n"))
max = max(num1,num2)
min = min(num1,num2)
func(min,max)
'''
# 2 List = [-2,1,3,-6],如何实现以绝对值大小从小到大将List中内容排序。
'''
print(sorted([-2,1,3,-6],key=abs))
'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)

n = int(input("请输入台阶个数:\n"))
print(fib(n))

