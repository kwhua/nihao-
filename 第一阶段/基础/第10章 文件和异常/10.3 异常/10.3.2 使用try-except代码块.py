'''
    当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。你让
Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。
    处理ZeroDivisionError异常的try-except代码块类似于下面这样：
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("0不能被除!!!")

'''
    我们将导致错误的代码行print(5/0)放在了一个try代码块中。如果try代码块中的代码运行
起来没有问题，Python将跳过except代码块；如果try代码块中的代码导致了错误，Python将查找
这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
    在这个示例中，try代码块中的代码引发了ZeroDivisionError异常，因此Python指出了该如
何解决问题的except代码块，并运行其中的代码。这样，用户看到的是一条友好的错误消息，而
不是traceback：
    0不能被除!!!
    
    
    如果try-except代码块后面还有其他代码，程序将接着运行，因为已经告诉了Python如何处
理这种错误。下面来看一个捕获错误后程序将继续运行的示例。
'''



