str1 = '请教作业'
s2 = str1.encode(encoding="gbk")
print(s2)  # b'\xc7\xeb\xbd\xcc\xd7\xf7\xd2\xb5'
s3 = s2.decode(encoding="gbk")
print(s3)  # 请教作业

# 九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%d"%(y,x,x*y),end="\t")
    print()


m1 = f"{2.823742984:0.2f}*{3}={6}"
print(m1)

n = eval(input('请输入一个整数：'))
s = str(n)
f = True

for i in range(len(s)//2):
    if s[i] != s[-1-i]:
        f = False
    break
if f:
    print('%d 是一个回文数' % n)

else:
    print('%d 不是一个回文数' % n)












num = int(input('请输入一个整数：'))
s = str(num)
mark = True
for x in range(len(num)):
    if s[x] != s[-x-1]:
        mark = False
if mark == True:
    print(f"{num}是回文数.")
else:
    print(f"{num}不是回文数.")

