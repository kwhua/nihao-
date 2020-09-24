'''
    使用Python写入文件时,需要以"w"、附加“a”或创建“x”模式打开文件。
需要谨慎使用“w”模式，因为会覆盖文件（如果文件已存在），改文件之前所有
的数据都将被删除。写入字符串或字节序列（对于二进制文件）是使用write（）
方法实现的，返回写入文件的字符数：
'''
# 写入字符串或字节序列（对于二进制文件）是使用write（）方法实现的，返回写入文件的字符数：
with open('example.txt', 'w') as f:  # 使用'w'模式
    print(f.write('I love Python'))
    print(f.write(' Hello!'))

with open('example.txt', 'a') as f:
    f.writelines(['Over and over', ' DealBreaker'])

#     再次打开文件"example.txt",会发现文件中的原先的数据,没有被删除,使用write()方法
# 写入的数据被追加到了原数据的结尾。
with open('example.txt', 'r') as f:
    print(f.read())
