class Person:
    max_age = 180

    def __init__(self,name):
        self.name = name

    def change_virtue(self):
        self.name = "张三"
        self.max_age = 210

    @classmethod
    def change_name(cls):
        print("    "  )

    @staticmethod
    def change_gender():
        print("      ")




zs = Person("zs")
print(zs.name)
zs.change_virtue()
print(zs.name)

Person.max_age = 200
print(zs.max_age)
zs.change_virtue()
print(zs.max_age)
ls = Person("ls")
print(ls.max_age)