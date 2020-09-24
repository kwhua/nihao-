


'''
    将文件读取到内存中后,就可以以任何方式使用这些数据了.下面以简单的方式使用圆周率
的值.首先,我们创建一个字符串,它包含文件中存储的所有数字,且没有任何空格:
'''
with open('pi_digits.txt') as f:
    lines = f.readlines()
# end=''
pi_string = ''
for line in lines :
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

# 注意:读取文本文件时,Python将其中的所有的文本都解读为字符串.如果你读取的是数字,并
# 要将其作为数值使用,就必须使用函数int()将其转换为整数,或用函数float()将其转
# 换为浮点数.