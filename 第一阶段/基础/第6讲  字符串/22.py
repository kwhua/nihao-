d = {1: 2}
s = "fsdf"
print(d == s)

n = 1


def func():
    global n  # 将声明为全局变量
    n = n + 1
    print(n)  # 21


func()
print(n)  # 21

num1 = int(input("请输入一个整数:\n"))
num2 = int(input("请输入一个整数:\n"))
max = max(num1,num2)
min = min(num1,num2)
lst = [x for x in range(min,max+1)]
def pingfang(x):
    return x**2
res = map(pingfang,lst)
lst2 = []
for x in res:
    lst2.append(x)
print(lst2)