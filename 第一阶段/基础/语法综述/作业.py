# （1）写一个正则表达式，使其能同时识别下面所有的字符串：'bat','bit', 'but', 'hat', 'hit', 'hut'
# re.findall".+t$"
# （2）匹配所有能够表示Python浮点数的字符串集
# （3）找出一个字符串中是否有连续的5个数字
import re

# （1）写一个正则表达式，使其能同时识别下面所有的字符串：'bat','bit', 'but', 'hat', 'hit', 'hut'
lst = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']

for x in lst:
    ret = re.match(".+t$", x)
    if ret:
        print(x)
    else:
        print(f"{x}不符合要求")

# （2）匹配所有能够表示Python浮点数的字符串集
ret1 = re.match(r"^(-?\d)+(.\d+)$","123.4234579096434567898654345678")
# ret1 = re.match(r"^(-?\d+)(\.\d+)?$","123.456.764576")
print(ret1.group())

# （3）找出一个字符串中是否有连续的5个数字

ret2 = re.search(r"(\d{5})","1234567642345576")
print(ret2)