'''
    使用文件时,一种常见的问题是找不到文件:你要查找的文件可能在其他地方、文件名
可能不正确或者这个根本不存在。对于所有这些情形，都可使用try-except代码块以直观
的方式进行处理。
    我们来尝试读取一个不存在的文件。下面的程序尝试读取文件alice.txt的内容,但是
我没将这个文件存储在-->文件和异常.py所在的目录中:
'''
# with open('alice.txt','r') as f:
#     contents = f.read()
# Python无法读取不存在的文件,因此它引发一个异常:
'''
Traceback (most recent call last):
  File "G:/Python/第一阶段/基础/第10章 文件和异常/10.3 异常/10.3.5 处理FileNotError 异常.py", line 8, in <module>
    with open('alice.txt','r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
'''
# 在上述的Traceback中,最后一行报告了FileNotFoundError异常,这是Python找不到要打开的文件
# 时创建的异常.在这个实例中,这个错误是函数open()导致的,因此要处理这个错误,必须将
# try语句放在open()代码行之前:
try:
    with open('alice.txt','r') as f:
        contents = f.read()
except FileNotFoundError:
    print("文件未创建,请先创建文件.")
'''
    在这个实例中,try代码块引发的FileNotFoundError异常,因此Python找到与该错误匹配的
except代码块,并运行其中的代码.最终的结果是显示一条友好的提示错误的消息,而不是Traceback:
    如果文件不存在,这个程序什么都不会做,因此错误处理的代码的意义不大.下面来扩展这个示例
看看在你使用多个文件时,异常处理可提供什么样的帮助.
'''