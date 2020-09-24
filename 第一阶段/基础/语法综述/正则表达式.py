import re

# 导入re模块

# match(patter,string) 从开始的位置开始匹配
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

# re.search()
# re.search()

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'\D*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)


# \b
print(re.findall(r'\bam\b', 'I am hamha'))  # ['am']
print(re.findall(r'am', 'I am hamha'))  # ['am', 'am']

# \B
print(re.findall(r'h&!\B', 'I &! h&!ha'))  # []
print(re.findall(r'&!\B', 'I &! h&!ha'))  # ['&!']


str = '010-11101014'
# ret = re.match("(\d{3})-(\d{7})",str)
ret = re.match("(\d+)-(\d+)",str)
print(ret.group())  # 010-1110101
print(ret.group(1))  # 010
print(ret.group(2))  # 1110101


s="This is a number 234-235-22-423"
r=re.match(".+(\d+-\d+-\d+-\d+)",s)  # 贪婪模式
print(r.group(1))  # 4-235-22-423

r=re.match(".+?(\d+-\d+-\d+-\d+)",s)  # 非贪婪模式
print(r.group(1))  # 234-235-22-423
