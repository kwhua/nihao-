# 字符串的序列操作
# 1.索引
str = "hello world"
print(str[2])  # l

# 2.切片
print(str[::1])  # hello world

# 3.拼接和重复
str1 = " Python!"
print((str + str1))  # hello world Python!
print(str * 2)  # hello worldhello world

# 4.赋值
a, *b = str
print(a)  # h
print(b)  # ello world

# 5.遍历
for x in str:
    print(x)

# 字符串的方法
# 注意严格区分大小写
# 查找
# find()
print(str.find("e"))  # 1

# rfind()
print(str.rfind("e"))  # 1

# index()
print(str.index("e"))  # 1

# rindex()
print(str.rindex("e"))  # 1

# count()
print(str.count("l"))  # 3

# 拆分
# partition() 返回一个元组
# 按item切割成 ("item前面","item自身","item后面")
print(str.partition("el"))  # ('h', 'el', 'lo world')

# splitlines 返回一个列表
# 按照行分割,返回一个包含各行作为元素的列表,按照换行符切
print(str.splitlines())  # ['hello world']

# split(item,maxsplit="")
# 按照指定的内容进行分割,maxsplit:默认将指定的所有的内容进行分割,可以指定maxsplit的值,
# 如果maxsplit=1 表示只按照第一个指定内容进行分割,后面剩余的不分割,如果括号里面不写东西,
# 默认是空(空格,换行符,制表符)进行切割
print(str.split("l", maxsplit=2))  # 'he', '', 'o world']

# 替换
# replace(item,count=)
# 从左往右替换指定的元素,可以指定替换的个数, 默认是全部替换
print(str.replace("l", 'L', 2))  # heLLo world

# 字符串的修饰符
# center(长度,item)
# 让字符串在指定长度居中,如果不能居中左短右长,可以指定填充内容, 默认空格填充
print(str.center(20, "-"))  # ----hello world-----
# ljust()
# 让字符串的长度左齐,可以指定填充内容,默认空格填充
print(str.ljust(20, "-"))  # hello world---------
# rjust()
# 让字符串的长度右齐,可以指定填充内容,默认空格填充
print(str.rjust(20, "-"))  # ---------hello world
# zfill
# 将字符串填充到指定长度,不足的地方使用0从左开始填充
print(str.zfill(20))  # 000000000hello world
# strip
# 默认取出两边的空格,取出的内容可以指定。item里面的内容是独立存在的
str1 = "_qh  ello world "
print(str1.strip('_qr'))  # h  ello world
# rstrip
# 默认取出右边的空格,取出的内容可以指定。item里面的内容是独立存在的
print(str1.rstrip('_qr'))  # _qh  ello world
# lstrip
# 默认取出左边的空格,取出的内容可以指定。item里面的内容是独立存在的
print(str1.lstrip('_qr'))  # h  ello world

# 交换key和value的值
dict1 = {'a': 1, 'b': 2, 'c': 3}
new_dict = dict()
for x, y in dict1.items():
    new_dict[y] = x
print(new_dict)

# get的方法,找到了返回value值,未找到,返回自定义的值
zs = {'name': 'zs', 'age': 20, 'height': 170}
print(zs.get("weight", "未找到键:weight"))  # 未找到键:weight

# 字符串的变形
# upper()  将字符串中所有的字母转换为大写
str2 = 'HeLlo wOrlD'
print(str2.upper())  # HELLO WORLD

# lower 将字符串中所有的字母转换为小写
str2 = 'HeLlo wOrlD'
print(str2.lower())  # hello world

# swapcase 将字符串里的大小写互换
str2 = 'HeLlo wOrlD'
print(str.swapcase())  # HELLO WORLD

# title 将字符串当中的单词首字母大写,单词以非字母划分
str2 = 'HeLlo wOrlD'
print(str2.title())  # Hello World

# capitlalize 只有字符串的首字母大写
str2 = 'HeLlo wOrlD'
print(str2.capitalize())  # Hello world

# expandtabs(num)
# 把字符串中的tab符号("\t")转换为空格,tab符号("\t")默认是8个空格,num为int,
str2 = "    "
print(str2.expandtabs(8))  # dl  hsd

# 输入一些符号,统计数字个数,字母字数,以及其他符号数量
# 输入字符串
# 数字的计数
num_count = 0
# 字母的计数
pha_count = 0
# 其他符号的计数
other_count = 0
# 随机输入字符串
str3 = input("随机输入字符串:\n")
# 遍历字符串
for x in str3:
    # 判断x是否是字母和数字还是其他符号
    boo = x.isalnum()
    # 如果是字母和数字
    if boo == True:
        # 判断是否是数字
        num = x.isdigit()
        # 如果是
        if num == True:
            num_count += 1
        #     不是
        else:
            pha_count += 1
    # 除字母和数字的其他符号
    else:
        other_count += 1
print(num_count)
print(pha_count)
print(other_count)


