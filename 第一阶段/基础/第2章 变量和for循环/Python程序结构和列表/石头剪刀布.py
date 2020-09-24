import random

# 1 - 石头  2 - 剪刀 3 - 布
# 电脑随机产生一个1~3的数字代表石头剪刀布
computer = random.randint(1, 3)
# 用户输入自己出的手势 将其匹配成手势相对应的数字
sign = input("请输入你的手势:[石头 剪刀 布]\n")
print()
if sign == '石头':
    sign = 1
if sign == '剪刀':
    sign = 2
if sign == '布':
    sign = 3
# 判断电脑和用户的输赢情况
if sign == 1 and computer == 2 \
        or sign == 2 and computer == 3 \
        or sign == 2 and computer == 1:
    print("恭喜你获胜!")
elif sign == 1 and computer == 1 \
        or sign == 2 and computer == 2 \
        or sign == 3 and computer == 3:
    print("平局.")
elif sign == 3 and computer == 2 \
        or sign == 1 and computer == 3 \
        or sign == 2 and computer == 1:
    print("你输了...")
else:
    print("输入有误!")

