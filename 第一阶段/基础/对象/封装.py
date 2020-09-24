class Person:
    '''自我介绍'''

    def __init__(self, name, gender, age, height, hometown):
        '''实例属性'''
        self.name = name
        self.gender = gender
        self.__age = age  # 私有属性
        self.height = height
        self.hometown = hometown

    def speak(self):
        return f'{self.name}在说话'
        # print(f'{self.name}在说话')

    def get_age(self):
        '''返回私有属性'''
        return self.__age


    def __str__(self):
        return self.speak()

    def __work(self):  # 私有制方法
        '''对象的工作'''
        print(f"{self.name}工作辛苦,每天搬砖.")


# 创建并初始化对象:男
zs = Person('zs', '男', 20, 170, '北京')
# 女
xiao_fang = Person("小芳", "女", 36, 175, "上海")

# 将年龄属性变成私有属性,不能访问
# print(zs.__age)

# 利用方法调用私有属性
print(xiao_fang.get_age())

# 直接访问私有属性和方法
print(xiao_fang._Person__age)
zs._Person__work()
# 类外部调用
print(zs)