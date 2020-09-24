a = 100


def func(n):
    print(n)
    n = 20
    print(n)


func(a)
print(a)


def func1(l=[]):
    for x in range(1, 4):
        l.append(x)
    print(l)  # 访问局部命名空间
    print(locals())


func1()
func1()

# 命名空间
a = 10
b = 20
name = 'zs'


def func():
    pass


# 全局命名空间
# c = {"a":10,"b":20,"name":"zs","func":function at id地址}


# 访问全局命名空间
print(globals())
print("-" * 50)

ac = id


def func():
    ac = id
    print(ac)


func()

a = 10


def x():
    a = 20
    print(a)

    def y():
        a = 30
        print(a)

    y()


x()




print("-"*50)

def fun():
    x =  1
    def fun1():
        nonlocal  x
        b =x+1
        print(b)
    fun1()
    print(x)
fun()



