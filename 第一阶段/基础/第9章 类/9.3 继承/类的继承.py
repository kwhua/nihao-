
""""
   编写类时,并非总是从空白开始.如果你编写的类是另一个现成类的特殊版本.可使用继承.
 一个类继承另一个类时,它将自动获得另一个类的所有属性和方法;原有的类称为父类,而新类
 称为子类.子类继承其父类的所有属性和方法,同时还可以定义自己的属性和方法.
"""
# 子类的方法 __init__()
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# 创建电动汽车的电瓶
class Battery:
    '一次模拟电动汽车电瓶的简单尝试'
    def __init__(self,battery_size=70):
        '初始化电瓶的属性'
        self.battery_size=battery_size
    def describe_battery(self):
        '打印一条描述电瓶容量的信息'
        print(f"This car has a {self.battery_size}-kwh battery")
    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85

    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270


        message=f"This car can go approximately {range}  miles on a full charge."
        return message

# 创建电动汽车的类
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""

        super().__init__(make,model,year)
        self.battery=Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.get_range())