a= 10

# 调用函数
# print_hello()

# 定义一个函数，实现打印hello world
def print_hello():
    """这是一个打印hello world的函数"""
    print("hello world")



# 调用函数
# print_hello()
#
# print_hello()


# 定义函数吃饭
def eat():
    """这是一个吃饭的函数"""
    print("吃饭")


# # 吃早饭
# eat()
# # 工作
# # 吃午饭
# eat()
# # 看电影
# # 吃晚饭
# eat()


c = eat  # 将函数eat赋值给c
c2 = eat()  #  将函数eat执行的结果赋值给变量c2
print(c2)
# print(c)
# print(eat)

# 调回函数c，相当于调用eat()
c()

print(type(c))

#
# eat()  # 调用函数eat
# eat  # eat函数本身

# 函数名和变量名本质？本质没有区别









