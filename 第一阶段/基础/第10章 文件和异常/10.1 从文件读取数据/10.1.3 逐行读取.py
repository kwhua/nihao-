



'''
    读取文件时，常常需要检查其中的每一行：你可能要在文件中查找特定的信息，或者要以
某种方式修改文件中的文本。例如，你可能要遍历一个包含天气数据的文件，并使用天气描述
中包含字样sunny的行。在新闻报道中，你可能会查找包含标签<headline>的行，并按特定的格
式设置它。
    要以每次一行的方式检查文件，可对文件对象使用for循环：
rstrip() : 清除空白
'''
with open('pi_digits.txt','r') as f:
    # 字节是计算机信息的计量单位.Python 3默认是 utf-8,中文占2-4个字节,英文占1字节.
    # 如果是读取整行文本 使用readline()方法:
    print(f.readline())  #  仅读取第一行
print("-"*50)

with open('pi_digits.txt','r') as f:
    # 如果想读取多行是: 括号里写的是读取几个字符
    for _ in range(3):
        print(f.readline())
print("-"*50)

with open('pi_digits.txt','r') as f:
    #  如果想要打印剩余的全部行,使用readlines()方法: 以列表的形式返回 而且会将换行读取出来
    print(f.readlines())

file_name='pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())