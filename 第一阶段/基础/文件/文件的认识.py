import os

file = open("你好,世界", mode="w", encoding="utf8")
lst = ["我的第一个文本文件\n", "12\n", "3"]
file.writelines(lst[:1:1])
file.close()

file1 = open("你好,世界", mode="r", encoding="utf8")
print(type(file1.read()))
file1.close()

file = open("你好,世界", "a", encoding="utf-8")
file.writelines("\nstudy hard  day day up")
file.close()

with open("你好,世界", "r", encoding="utf8") as f:
    print(f.readline(20))

f = open("你好,世界", "w", encoding="utf8")
f.write("hello world")
f.close()


# 遍历目录
def print_file(path):
    """打印文件"""
    file_list = os.listdir(path)
    # 查看目录下所有的文件
    for f in file_list:  # 遍历目录下的所有文件
        new_file = os.path.join(file_list, f)
        # 将目录的路径与文件名进行拼接,变成文件的路径

        if os.path.isdir(new_file):
            # 判断文件是否是文件夹
            print_file(new_file)
        #     如果是,将它作为路径放入函数中
        else:
            print(new_file)
#             如果不是,将其打印
