import os

# os.rename("CSV文件.csv","csv文件.csv")
# os.mkdir("a")
# os.makedirs("a1/a2/a3/a4")

# os.rmdir("a")
# os.removedirs("a1/a2/a3/a4")
# 获取当前地址
print(os.getcwd())

# 获取当前列表目录
print(os.listdir("."))

# 更改所在路径
os.chdir("..")
print(os.getcwd())