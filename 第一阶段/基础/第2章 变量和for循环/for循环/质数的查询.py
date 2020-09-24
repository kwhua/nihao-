# num = int(input("请输入一个数:\n"))
# x = 2
# while x < num:
#     if num % x == 0:
#         print(f"{num}不是质数.")
#         break
#     x += 1
# else:
#     print(f"{num}是质数.")

# num = int(input("请输入一个数:\n"))
# for y in range(2, num):
#     if num % y == 0:
#         print(f'{num}不是质数')
#         break
# else:
#     print(f"{num}是质数")

for x in range(10):
    print(x)

# 输出一行* * * * * *
for x in range(1):
    for y in range(6):
        print("*",end=" ")
    print()
print("-"*50)

# 输出
'''
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
'''
for x in range(6):
    for y in range(6):
        print("*",end=' ')
    print()
print("-"*50)

# 打印
'''
*
* *
* * * 
* * * *
* * * * *
* * * * * *
'''
for x in range(6):
    for y in range(x+1):
        print("*",end=" ")
    print()
