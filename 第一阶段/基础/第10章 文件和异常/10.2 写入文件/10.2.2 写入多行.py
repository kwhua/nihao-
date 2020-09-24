
'''
    函数write()不会在你写入的文本末尾添加换行符，因此如果你写入多行时没有指定换行符，
文件看起来可能不是你希望的那样：
'''
with open('nihao.txt','w') as f:
    f.write("I love Python!\n")
    f.write("I love java!\n")

# 当然你也可以使用空格、制表符和空行来设置这些输出的格式。