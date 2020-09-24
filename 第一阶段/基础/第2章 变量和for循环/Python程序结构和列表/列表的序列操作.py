"""import random

print("人和电脑猜拳大赛,三胜制.")
mark = True
count = 0
computer_count = 0
people_count = 0
while mark:
    computer_geste = random.randint(1, 3)
    people_geste = input("请输入你手势:[石头/剪刀/布]\n")
    if people_geste == '石头':
        people_geste = 1
    elif people_geste == '剪刀':
        people_geste = 2
    else:
        people_geste = 3
    count += 1
    if (people_geste == 1 and computer_geste == 2) \
            or (people_geste == 2 and computer_geste == 3) \
            or (people_geste == 3 and computer_geste == 1):
        people_count += 1
        if people_count <= 2:
            print(f"第{count}局,你获胜!你已获胜{people_count}局.")
        else:
            print(f"你已获胜{people_count}局,恭喜你获得最后的胜利!")
            mark = False
    elif people_geste == computer_geste:
        print(f"第{count}局,平局!")
    else:
        computer_count += 1
        if computer_count <= 2:
            print(f"第{count}局,电脑获胜!电脑已获胜{computer_count}局.")
        else:
            print(f"电脑已获胜{computer_count}局,恭喜电脑获得最后的胜利!")
            mark = False
"""
# 猜年龄游戏
# 如果猜对了，打印恭喜信息并退出。允许用户最多尝试3次，3次都没猜对的话，就直接退出。
'''
import random

for x in range(3):
    random_age = random.randint(1,100)
    age = int(input("请输入你猜想的年龄[100以内的]:\n"))
    if x <= 1:
        if age == random_age:
            print(f"恭喜你才对了,共用了{x}次机会.")
            break
        elif age > random_age:
            print(f"猜大了,往小的猜,还剩{2 - x}次机会.")
        else:
            print(f"猜小了,往大的猜,还剩{2 - x}次机会.")
    else:
        print("3次机会用完了,正在退出...")
'''
# 打印九九乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{y} * {x} = {x * y}", end=" \t")
    print()
