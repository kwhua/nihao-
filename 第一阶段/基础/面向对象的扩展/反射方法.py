# class Person:
#     max_age = 120
#
#     def __init__(self, age):
#         self.age = age
#
#     def walk(self):
#         print("walk")
#
#     def run(self):
#         print("run")
#
#     def sing(self):
#         print("sing")
#
#     def dance(self):
#         print("dance")
#
#
# zs = Person(20)
# choice = input("请输入方法的名称>>>>>")
# if hasattr(zs, choice):
#     method_ = getattr(zs, choice)
#     if callable(method_):
#         method_()
#     else:
#         print(method_)
#
# else:
#     print("输入有误")


class Shopping_cart:
    __commodity = None

    def __new__(cls, *args, **kwargs):
        if not cls.__commodity:
            cls.__commodity = object.__new__(cls)
        return cls.__commodity

    def __init__(self):
        self.cart = []


class Person:

    def add_(self, name,cart):
        cart.append(name)


cart1 = Shopping_cart()
cart2 = Shopping_cart()
cart3 = Shopping_cart()
cart4 = Shopping_cart()


ls = Person()


ls.add_(cart1.cart,"iPhone 11")
ls.add_(cart2.cart,"mate book")
ls.add_(cart3.cart,"mi x20")
ls.add_(cart4.cart,"find x")