# 闭包
def func():
    msg = "hello world"
    def inner():
        print(msg)
    return inner
def func1():
    msg = "你好,世界"
    def inner():
        print(msg)
    return inner

f1 = func()
f2 = func1()
f1()
f2()

a  =10
# 装饰器
def func(fn):
    # fn为外部函数
    def inner():
        # 执行指定功能前的需要做的事
        print("执行指定功能前的需要做的事")
        fn()
        # 执行指定功能后的需要做的事
        print("执行指定功能后的需要做的事")
    return inner
@func  # f = func(f)
def f():
    print("这是f函数.")

f()