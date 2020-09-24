import re

s = "This is a number 234-235-22-423"
r = re.match(".+(\d+-\d+-\d+-\d+)", s)  # 贪婪模式
print(r.group(1))  # 4-235-22-423

r = re.match(".+?(\d+-\d+-\d+-\d+)", s)  # 非贪婪模式
print(r.group(1))  # 234-235-22-423
