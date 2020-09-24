

'''
导入类
    随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦如此。为遵循
Python的总体理念，应让文件尽可能整洁。为在这方面提供帮助，Python允许你将类存储在模块
中，然后在主程序中导入所需的模块。
'''
# 1,导入单个类
from 类的继承 import Car
my_new_car=Car('Tesla','module l',2020)
print(my_new_car.get_descriptive_name())
print("-"*50)
print("\n")
# 2,在一个模块中存储多个类
from 类的继承 import ElectricCar
my_tesla=ElectricCar('Tesla','module l',2020)
print( my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.get_range())

print("\n")
# 3,从一个模块中导入多个类 form 模块名 import 类1,类2...类3
# 例:
from 类的继承 import Car,ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

print("\n")
# 4,导入模块中所有的类  from module_name import *
from 类的继承 import *


