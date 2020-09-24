'''
  面对对象编程是最有效的软件编写方法之一.在面向对象编程中,你编写表示显示世界中的失误和情景的类,并基于这些类来创建对象.

'''


# 创建和使用类 类可以模仿任何的东西.

# 例如:创建一个狗的类
class Dog():  # 在Python中类名的首字母一般是大写
    # 一次模拟小狗的尝试
    # 定义小狗的信息
    def __init__(self, name, age, gender):  # 使用init的方法
        self.name = name
        self.age = age
        self.gender = gender

    #     模拟小狗被命令时蹲下
    def sit(self):
        print(self.name.title() + " is now sitting.")

    #     模拟小狗被命令时打滚
    def roll_about(self):
        print(self.name.title() + " is now rolled over")


my_dog = Dog("namei", 5, "women")
print("My dog's name is " + my_dog.name.title() + ".")
print(f"My dog's age is {my_dog.age} year old.")
my_dog.sit()
my_dog.roll_about()


# 例:
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name's :" + self.name.title() + '.')
        print(self.name.title() + " restaurant cuisine type is " + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        print("The " + self.name.title() + " restaurant is open from Monday to Friday.")


restaurant = Restaurant("gongfu", "Chineseflavor")
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 例:
class Car():
    def __init__(self, name, year, model, mileage):
        self.name = name
        self.year = year
        self.type = model
        self.mileage = mileage

    def get_descriptive(self):
        car_name = f"{self.year.title()} {self.name.title()} {self.type.title()}"
        return car_name

    def add_mileage(self, miles):
        if miles >= 0:
            self.mileage += miles
        else:
            print("inputError!")

    def read_mileage(self):
        print(f"This car has {self.mileage} miles on it.")


m = int(input("请输入公里数:\n"))
k = int(input("请输入增加的公里数:\n"))
my_car = Car(name='Audi', year="2019", model="A8L", mileage=m)

print(my_car.get_descriptive())
my_car.add_mileage(miles=k)
my_car.read_mileage()


# 例:尝试登录
class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print("my name's " + self.first_name + self.last_name)

    def greet_user(self):
        print(self.first_name + self.last_name + " hello nice to meet you!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


my_name = User("Kuang", "wenhua", 1)
my_name.describe_user()
my_name.greet_user()
my_name.increment_login_attempts()
my_name.increment_login_attempts()
my_name.increment_login_attempts()
my_name.increment_login_attempts()
my_name.increment_login_attempts()
print(my_name.increment_login_attempts())
print(my_name.reset_login_attempts())
