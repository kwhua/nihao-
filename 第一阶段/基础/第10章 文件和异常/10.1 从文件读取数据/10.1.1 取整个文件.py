


"""
    要读取文件，需要一个包含几行文本的文件。下面首先来创建一个文件，它包含精确到小数
点后30位的圆周率值，且在小数点后每10位处都换行：
使用with open将pi_digits.txt打开 ,as 存储在file_object文件中
"""
with open('pi_digits.txt','r') as f:
    # 将file_object的内容阅读并保存在contents中
    # 文件对象的read()方法用于读取文件,当不传递任何参数时,read()方法将读取整个文件:

    print(f.read())
print("-"*50)

with open('pi_digits.txt','r') as f:
    # read()方法也可以通过传递参数来指定读取的字节数:
    print(f.read(8))
print("-"*50)




