# 输出1-10
x = 1
while x <= 10:
    print(x)
    x += 1
print("-" * 50)

# 输出1-10的和
x = 1
sum = 0
while x <= 10:
    sum += x
    x += 1
print(sum)
print()

x = 0
while x < 20:
    x += 1
    if x == 10:
        continue

    print(x)
print()
ticket = 11
while ticket > 0:
    ticket -= 1

    if ticket == 6:
        print("第5张票是预留票,不售!")
        continue
    if ticket == 0 :
        break

    print(f"现在是第{11 - ticket}张,还剩{ticket-1}张.")
    if ticket == 1 :
        print("票已售完!")
        continue