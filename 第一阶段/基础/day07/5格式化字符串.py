"""
模板
"num1 * num2 = num3"
"""
# i = 2
# j = 3
# print(i,"*",j,"=",i*j)  # 2*3= 6  写法不方便

# 九九乘法表模板
# m = "%d*%d=%d"
# print(m)
# print(m%(2,3,6))
# print(m%(3,3,9))

# 练习：自我介绍，姓名小米，年龄 18, 身高1.75米，体重70kg,目前的学习进度为80%。使用字符串格式化将内容输出到控制台

name = "小米"
age = 18
height = 1.75
weight = 70

print("我叫%s,我今年%d,我的身高是%.2f,我的体重是%d,学习进度是%d%%"%(name,age,height,weight,80))


# format()
"""
模板
"{} * {} = {}"
"""
# print(i,"*",j,"=",i*j)  # 2*3= 6  写法不方便

# print("{}*{}={}".format(2,3,6))  # 2*3=6
# # 编号
# print("{0}*{2}={1}".format(2,3,6))  # 2*6=3
# print("{0}*{1}={1}".format(2,3,6))  # 2*3=3
# print("{1}*{1}={1}".format(2,3,6))  # 3*3=3

# 错误：超过了最大索引值
# print("{1}*{1}={4}".format(2,3,6))  # 3*3=3
# 编号和不编号混用
# print("{1}*{}={}".format(2,3,6))


# 2 给占位符起名字
m4 = "{num1}*{num2}={value}"  # ValueError
# print(m4.format(5,2,10))
print(m4.format(num2=5,num1=2,value=10))
# print(m4.format(num2=5,value=10,num1=2,))


# 3 填充与格式化
# 格式： :[填充字符][对齐方式 <^>][最小宽度]
# < 表示向左对齐， ^表示居中对齐， >表示向右对齐
# """
# m = "{:$>10}*{:#<3}={}"
# print(m.format(5,2,10))

# 4 精度控制
# 字符串长度为10位，居中对齐，不够用# 填充，小数点后保留两位
# print("{:#^10.2f}".format(2.34246546))
# print("{:#^10.2f}".format(2.34946546))  # 四舍五入规则


# f-string
# m = "{2}*{3}={6}"
# m2 = f"{6}*{3}={18}"

# num = 100
# num2 = 55
# print(m)
# print(m2)
# print(f"{num}*{num2}={num*num2}")

# 打印九九乘法表对比
# for i in range(1,10):
#     for j in range(1,i+1):
#         # print(j,"*",i,"=",i*j,end='\t') # 不使用格式化
#         # print("%d*%d=%d"%(j,i,i*j),end='\t')  # 使用%方式
#         # print("{}*{}={}".format(j,i,i*j),end='\t') # 使用format形式
#         print(f"{j}*{i}={i*j}",end='\t')  # 使用f-string形式
#     print()