# startswith
s = "hello world"

print(s.startswith("hel"))  # True
print(s.startswith(" hel"))  # False

print(s.startswith(" wo"))  # False

#  判定从索引5到10之间的字符串是否以“ wo”开头
print(s.startswith(" wo",5,10))  # True


# 需求：用户输入一些符号，请统计数字个数，字母个数，以及其他符号数量。
my_str = input("随便输入一些符号：")
num_count = 0
alp_count = 0
other_count = 0

for i in my_str:
    if i.isdigit():
        num_count += 1
    elif i.isalpha():
        alp_count += 1
    else:
        other_count += 1

print("数字有",num_count)
print("字母有",alp_count)
print("其他有",other_count)