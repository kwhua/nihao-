"""
1 位置参数
2 关键字参数
3 默认参数
4 可变参数
    4.1 元组类型的可变
    4.2 字典类型的可变
"""

# 1 位置参数：实参传递的顺序按照形参定义的顺序进行传递的传参方式

# 需求定义一个函数，给定两个数字，遍历两个数字之间的所有数字
def func2(num1,num2):
    """打印num1到num2之间的数字"""
    for i in range(num1,num2+1):
        print(i,end=" ")

# 使用位置参数调用
# func2(10,100)  # num1=10 ,num2=100
# func2(100,10)  # num1=100 ,num2=10

# 2 关键字参数(函数调用时使用)
# 使用关键字方式调用
# func2(num1=10,num2=100)
# func2(num2=100,num1=10)

# 默认参数（在定义时候体现）
def func3(num1,num2=100):
    """打印num1到num2之间的数字"""
    for i in range(num1,num2+1):
        print(i,end=" ")

# 调用
# func3(50,200)  # num1=50 num2=200
# func3(50)  # num1=50 num2=100


# 定义函数：自我介绍
def introduce(name,age,gender="男"):
# def introduce(gender="男",name,age):  # 错误
    print(f"我叫{name},今年{age}岁，性别是{gender}")

# 男生不需要输入性别
# introduce("zs",18,)
# introduce("ls",20,)
# introduce("ww",21,)
...
# 女生必须输入性别
# introduce("小花",18,"女")



# *args:元组类型
def introduce2(*args):
    print(args)
    print(f"我叫{args[0]},今年{args[1]}岁，身高是{args[2]}")


# introduce2("zs",20,170)
# introduce2("zs",20,170,weight=60)   # 错误


# **kwargs:字典类型可变参数
def introduce3(**kwargs):
    print(kwargs)
    # print(f"我叫{args[0]},今年{args[1]}岁，身高是{args[2]}")


#
def func4(*args,**kwargs):
    print(args)
    print(kwargs)
    # print(f"我叫{args[0]},今年{args[1]}岁，身高是{args[2]}")


func4(1,2,3,4,5,"86",name="zs",age=20)




"""
- 在定义函数时：位置参数-- 默认参数和*args---**kwargs
- 在调用函数时：位置参数---关键字参数
"""

# def f(name,age=20,*args,**kwargs):
def f(name,*args,age=20,**kwargs):
    pass