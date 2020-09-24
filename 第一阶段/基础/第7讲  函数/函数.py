# 输入两个数,输出两个数之间的数
def traverse(x: int, y=100):
    if x < y:
        for i in range(x, y + 1):
            print(i, end=" ")
    else:
        for i in range(y, x + 1):
            print(i, end=" ")

traverse(21)
print()

str1 = '2018-11-12'
str2 = str1.replace("-","")
print(str2)
print(f"{str2}中一共有{str2.count('1')}个1")