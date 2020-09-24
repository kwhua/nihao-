import csv
import os
# 打开文件
file = open("CSV文件.csv","r",encoding="utf8")


# 读取文件内容
csv_file = csv.reader(file)
print(list(csv_file))

for i in  csv_file:
    print(i)

# 关闭文件
file.close()






