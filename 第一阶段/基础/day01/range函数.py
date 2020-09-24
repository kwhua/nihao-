'''
range(m,n,step)
从m到n  不包括n  步长step


'''
# for x in range(0,20):
#     print(x)
# sum = 0
# for x in range(1, 101):
#     sum = sum + x
#     print(sum)
for x in range(1, 10):
    for y in range(1, x+1):
        print(f"{y}*{x}={x * y}",end="\t")
    print()
sum = 0
for x in range(1,101):
    # 偶数做减处理
    if x%2==0:
        sum -= x
    # 奇数做加处理
    else:
        sum += x
print(sum)


