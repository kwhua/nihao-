'''
结构:
    for x in 可迭代对象:
        循环内容
    else:
        代码
执行过程:执行循环的内容 ,如果循环正常结束,在执行else里面的代码

break :强制结束整个循环
continue:结束当前的一次循环
'''
# for x in range(1,6):
#     if x ==2:
#         break
#     print(x)
# else:
#     print("当前循环结束")

# 用户登录
for x in range(1, 6):
    a = int(input("请输入密码:\n"))
    if a == 123456:
        print("密码正确,欢迎登录")
        break
    elif not(x ==5):
        print(f"密码错误,还剩{5 - x}次")
else :
    print("五次机会以用完,请一个小时后重试")
