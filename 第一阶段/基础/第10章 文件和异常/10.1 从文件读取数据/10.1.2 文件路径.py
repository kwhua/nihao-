


'''
当你将类似pi_digits.txt这样的简单文件名传递给函数open()时，Python将在当前执行的文件
（即.py程序文件）所在的目录中查找文件。
根据你组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。例如，你可能将
程序文件存储在了文件夹python_work中，而在文件夹python_work中，有一个名为text_files的文
件夹，用于存储程序文件操作的文本文件。虽然文件夹text_files包含在文件夹python_work中，但
仅向open()传递位于该文件夹中的文件的名称也不可行，因为Python只在文件夹python_work中查
找，而不会在其子文件夹text_files中查找。要让Python打开不与程序文件位于同一个目录中的文
件，需要提供文件路径，它让Python到系统的特定位置去查找。
由于文件夹text_files位于文件夹python_work中，因此可使用相对文件路径来打开该文件夹中
的文件。相对文件路径让Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目
录的。在Linux和OS X中，你可以这样编写代码：是斜杠(/)
with open('../写入文件/example.txt') as file_object:
'''
# 在windows中是反斜杠(/)
# 相对路径(相对于此文件的路径)
# with open('..\写入文件\example.txt') as file_object:
# 绝对路径(电脑中它的位置)
# with open('G:\Python\基础\文件和异常\写入文件\example.txt') as file_object:

# 注意 : Windows系统优势能够正确解读文件路径的斜杠.如果你使用的Windows系统,且结果不符合预期
# 请确保文件路径中使用的是反斜杠.

