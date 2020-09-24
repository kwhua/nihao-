a,b,c,d= 1,2,3,4
_m = 100  # 私有变量.如果使用form 模块 import * 不会被导入,如果是精准导入可以
def f():
    pass
def f2():
    pass
def f3():
    pass

# 控制哪些对象是可以被导出的 __all__
# 必须用字符串包裹,使用()包裹元素
__all__ =('a','c','f')
import sys

print(sys.path)