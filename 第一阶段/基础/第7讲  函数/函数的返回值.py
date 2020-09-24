# 给定一个整数,返回从1到数字的之间的和
# 一个返回值
def add_(n):
    "两个数之间的数字求和"
    sum = 0
    for x in range(1,n+1):
        sum += x
    return sum

sum = add_(20)
print(sum)

def func2():
    return 1,1.5,1,'a',[1,2],(1,2),{1:2},{1,2}
res = func2()  #返回值为元组
print(res)


def func(diameter):
    pi = 3.14159265859
    area = pi*diameter**2
    girth = 2*pi*diameter
    return area,girth
diameter = int(input("请输入半径:\n"))
area,girth = func(diameter)
print(f"半径为{diameter}的圆,面积为{area:.2f}")
print(f"半径为{diameter}的圆,周长为{girth:.2f}")
