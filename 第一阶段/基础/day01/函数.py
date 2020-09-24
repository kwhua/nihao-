def hello_w(name):
    print("hello,world", name)


hello_w("Python")

print("-" * 50)


def display_message():
    print("学习了函数")


display_message()
print("-" * 50)


def favorite_book(title):
    print("我最爱的书是:", title)


favorite_book("简爱")
print("-" * 50)
# 无参有返回值
'''
def personal_summary():
    a = input("请输入你的姓名:\n")
    b = input("请输入你的年龄:\n")
    c = input("请输入你的身高:\n")
    d = input("请输入你的地址:\n")
    personal="我的姓名是:"+a+"年龄:"+b+"身高:"+c+"地址:"+d
    return personal
names=personal_summary()
print(names)
'''
print("-" * 50)
# 有参无返回值
# 交换两个变量的值
def change_num(nums):
    c =nums[0]
    nums[0] = nums[1]
    nums[1] = c
a = int(input("请输入一个数:\n"))
b = int(input("请输入一个数:\n"))
nums = [0,1]
nums[0]=a
nums[1]=b
change_num(nums)
a=nums[0]
b=nums[1]
print(a)
print(b)
# 有参有返回值
def get_max(x,y,z):
    if x>y and x>z:
        max=x
    elif y>x and y>z:
        max=y
    else:
        max=z
    return max
a = int(input("请输入一个数字:\n"))
b = int(input("请输入一个数字:\n"))
c = int(input("请输入一个数字:\n"))
max = get_max(a,b,c)
print()
print(max)
# 给数组添加元素
print("-"*50)
nums[4]=[]
# nums[0]=1
# nums[1]=2
# nums[2]=3
# nums[3]=4
print(len(nums))
