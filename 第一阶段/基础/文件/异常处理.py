import os

try:
    pass

except Exception as e:
    print(e)

# 判断文件或目录是否存在

print(os.path.exists("../笔记"))
print(os.path.exists("os模块.py"))


try:
    print(1/0)

# except Exception as e:
#     print(e)

finally:
    print(2)

