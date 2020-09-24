import csv

# 编写文件
file = open("CSV文件.csv", "w", encoding="utf8",newline="")

# 转换csv对象
csv_file = csv.writer(file)

# 写表头
csv_file.writerow(["姓名","年龄","性别"])

# 写数据
# csv_file.writerow(["张三",20,"男"])
# csv_file.writerow(["李四",25,"男"])
# csv_file.writerow(["王五",26,"男"])
# csv_file.writerow(["马汉",29,"男"])
# csv_file.writerow(["周瑜",24,"男"])
# csv_file.writerow(["小乔",26,"女"])

csv_file.writerows(
    [
    ["张三",20,"男"],
    ["李四",25,"男"],
    ["王五",26,"男"],
    ["马汉",29,"男"],
    ["周瑜",24,"男"],
    ["小乔",26,"女"]
]
)
# 关闭文件
file.close()   