'''
    使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外
访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该
列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
    下面的示例在with代码块中将文件pi_digits.txt的各行存储在一个列表中，再在with代码块外
打印它们：
'''
file_name = 'pi_digits.txt'
with open(file_name) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
