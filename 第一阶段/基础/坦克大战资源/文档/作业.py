
# 1打印指定路径下的所有文件名
import os
def print_file(path):
    """打印文件"""
    # 查看当前目录下所有文件
    file_list = os.listdir(path)
    # 遍历每个文件
    for f in file_list:
        # 改变path路径
        new_path = os.path.join(path,f)
        # 判断是否为目录
        if os.path.isdir(new_path):
            print_file(new_path)
        else:
            print(new_path)

print_file(r'C:\Users\李耀辉\Desktop\python0831\笔记')


# 2给指定路径下的所有文件重命名
import os
def rename_file(path):
    """重命名文件"""
    # 查看当前目录下所有文件
    file_list = os.listdir(path)
    # 遍历每个文件
    for f in file_list:
        # 改变path路径
        new_path = os.path.join(path,f)
        # 判断是否为目录
        if os.path.isdir(new_path):
            rename_file(new_path)
            pass
        else:
            # 获取文件名
            basename = os.path.basename(new_path)
            # 获取路径
            dirname = os.path.dirname(new_path)
            # 修改文件名
            new_name = basename[1:]
            # 重新拼接路径
            change_path = os.path.join(dirname,new_name)
            # 重命名
            os.rename(new_path,change_path)


rename_file(r'C:\Users\李耀辉\Desktop\笔记')