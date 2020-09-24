'''
    下面来看一种导致Python引发异常的简单错误。你可能知道不能将一个数字除以0，
但是我们还是让Python这样做吧：
'''
print(5/0)
'''
Traceback (most recent call last):
  File "G:/Python/第一阶段/基础/第10章 文件和异常/10.3 异常/10.3.1 处理ZeroDivisionError异常.py", line 5, in <module>
    print(5/0)
①ZeroDivisionError: division by zero
'''
'''
    在上述traceback中，①处指出的错误ZeroDivisionError是一个异常对象。Python无法按你的
要求做时，就会创建这种对象。在这种情况下，Python将停止运行程序，并指出引发了哪种异常，
而我们可根据这些信息对程序进行修改。下面我们将告诉Python，发生这种错误时怎么办；这样，
如果再次发生这样的错误，我们就有备无患了。
'''