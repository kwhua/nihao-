class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(f"{self.name}被调用了")

    def __del__(self):
        print(f"{self.name}被销毁")


ke = Person("lk", 18)
# print(ke.name)
# ke()  # 实例对象被当做方法调用
# print("=====================")
# del ke


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """实现等于或不等于"""
        if self.age == other.age:
            return True
        else:
            return False

    def __lt__(self, other):
        """实现小于或大于"""
        if self.age < other.age:
            return True
        else:
            return False


    def __le__(self, other):
        """实现小于等于或大于等于"""
        if self.age<= other.age:
            return  True
        else:
            return False




zs = Person('zs', 200)
ls = Person('ls', 20)
print(zs == ls)
print(zs > ls )