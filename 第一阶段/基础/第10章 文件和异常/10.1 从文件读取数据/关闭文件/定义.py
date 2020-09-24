

'''
    完成对文件的操作后,需要正确关闭文件.关闭文件将释放与该文件绑定的资源,
可以使用close()方法来完成:
    f=open('example.TXT')
    f.closeed  #  closed是文件的一个属性
    False
    f.close()  #  使用close()方法来关闭文件
    f.closed
    True
    通过这种方法来关闭文件并不是绝对安全的.如果文件执行某些操作时发生异常,
name程序将退出而不会关闭文件.try-finally语句可以很好地解决执行代码时发生
异常的问题,其结构大致如下:
    try:
        f=open('example.TXT')
#         执行一些关于文件的相关操作
    finally:
        f.close()
最好是使用with语句:
    with open('example.TXT') as f:
        pass  #  执行一些文件相关操作
    这种方法不需要显示调用close()方法,它是在内部完成的.
'''