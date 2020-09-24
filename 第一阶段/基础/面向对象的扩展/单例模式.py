class Card:
    __content = None
    def __new__(cls):
        if not cls.__content:
            cls.__content=object.__new__(cls)
        return cls.__content

    def __init__(self):
        self.card = []

class Person:
    """用户类"""
    def add_card(self,card,name):
        card.append(name)

iphone = Card()
hw = Card()
xiao_mi = Card()

# 创建用户
zs = Person()

zs.add_card(iphone.card,'iPhone 11')
zs.add_card(hw.card,'华为 P30')
zs.add_card(xiao_mi.card,'小米 mate X')


print(iphone.card)  # 查看苹果的购物车
print(hw.card)  # 查看华为的购物车