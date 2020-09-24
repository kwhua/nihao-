class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"我是{self.brand}")

    def move(self):
        print(f"{self.brand}会跑.")


class BMW(Vehicle):
    def move(self):
        print(self.brand, "嗖嗖的跑")


class Benz(Vehicle):
    pass


BMW = BMW("宝马")


# 描述人类
class Person:
    """描述人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skin = "blank"

    def speak(self):
        print("每个人都会说话")


class Chinese(Person):
    """描述中国人"""

    # def __init__(self):
    #     self.hometowm = "北京"

    def __init__(self, hometown, name, age):
        """增加中国人家乡属性"""
        self.hometown = hometown
        self.skin = "yellow"
        super().__init__(name, age)  # 手动调用父类方法


# 没有重写init方法：李老师具有姓名和年龄属性
# li = Chinese('李老师', 20)
# li.speak()

# 重写init方法,没有调用父类init方法：李老师没有年龄和姓名属性
# li = Chinese()
# li.speak()
# print(li.name)

# 重写父类init方法，且调用了父类的init方法：李老师具有父类的属性和自己扩展属性
li = Chinese('河北', 'li', 25)
print(li.name)
print(li.skin)  # 为什么不是yellow? 因为皮肤定义后,被调用Person属性的时候被覆盖了
print(li.hometown)
