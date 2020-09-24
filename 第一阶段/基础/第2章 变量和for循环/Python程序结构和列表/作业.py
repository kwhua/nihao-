# 商城项目菜单跳转，用户的登录

# print("欢迎光临淘宝网")
# operation = input("请输入你需要的功能:[注册/登录/退出]\n")
# if operation == '注册':
#     id = input("注册的账号:\n")
#     pwd = input("请输入账号的密码:\n")
#     print(f"你的{id}注册成功!")
# elif operation == '登录':
#     id = '123456'
#     pwd = '123'
#     input_id = input("输入你的账号:\n")
#     input_pwd = input("请输入账号的密码:\n")
#     if id == input_id and pwd == input_pwd:
#         print("欢迎登录!")
#     else:
#         print("账号或密码错误!")
# elif operation == '退出':
#         print("正在退出...")
# else:
#     print("输入不合法!")

# 输入一个考试分数，判断考试结果是否为通过，如果分数>=60,通过，否则，结果为不通过


# score = float(input("请输入你的分数:\n"))
# if 0 <= score <=100:
#     if score >=60 :
#         print("恭喜考试通过!")
#     else :
#         print("考试不通过,要努力加油了.")
# else :
#     print("输入的成绩不合法!")


# 1-100之间所有偶数的和
# x = 0
# sum_ = 0  #  定义一个sum_变量用来存储和
# while x <= 100 :
#     sum_ += x
#     x += 2
# print(f"1-100之间所有偶数的和为:{sum_}")

# 计算100到200范围内能被7或者9整除的数的个数。
# x = 100
# count = 0  #  定义count用来保存个数
# while x <= 200:
#     if x % 7 == 0 or x % 9 == 0 :
#         count += 1
#     x += 1
# print(f"100到200范围内能被7或者9整除的数的个数:{count}")

# 2019年 中国GDP：15.54万亿美元  美国GDP：21.41万亿美元GDP增长率6.1%，美国增长率2%，问在哪一年中国GDP超越美国？
chinese_gdp = 15.54
american_gdp = 21.41
year = 0
while year >= 0:
    year += 1
    chinese_gdp  *= 1.061
    american_gdp *= 1.02
    if chinese_gdp>= american_gdp:
        print(f"中国GDP将在{2019 + year}年超过美国.")
        break


# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数。
# ​	例如：一個52公斤的人，身高是155cm，则BMI为 :
# ​	52(kg)/1.55**2(m)= 21.6
# ​	BMI指数：
# ​	低于18.5：过轻
# ​	18.5-25：正常
# ​	25--28：过重
# ​	28-32：肥胖
# ​	高于32：严重肥胖
# height = float(input("请输入你的身高:[m]\n"))
# weight = float(input("请输入你的体重:[kg]\n"))
# BMI = weight / height ** 2
# if BMI <= 18.5:
#     print(f"你的BMI值为:{'{:.2f}'.format(BMI)},体重过轻.")
# elif 18.5 < BMI <= 25:
#     print(f"你的BMI值为:{'{:.2f}'.format(BMI)},体重正常.")
# elif 25 < BMI <= 28:
#     print(f"你的BMI值为:{'{:.2f}'.format(BMI)},体重过重.")
# elif 28 < BMI <= 32:
#     print(f"你的BMI值为:{'{:.2f}'.format(BMI)},体重肥胖.")
# else:
#     print(f"你的BMI值为:{'{:.2f}'.format(BMI)},体重过于肥胖.")
