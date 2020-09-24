'''
英雄联盟的英雄
属性:血量hp,名字name,蓝量mp,伤害damage,移速speed
方法:移动remove,跳舞dancing,攻击敌人attack,回城back
'''
class Hero:
    def __init__(self,hp,name,mp,damage,speed):
        self.hp = hp
        self.name = name
        self.mp = mp
        self.damage = damage
        self.speed = speed

    def remove(self):
        print(f"{self.name}移动了.")

    def dancing(self):
        print(f"{self.name}在跳舞.")

    def attack(self,enemy):
        count = 1
        while True:
            print(f'第{count}局'.center(42," "))
            print(f"来自于{self.name}和{enemy.name}之间的solo.")

            print(f"{self.name}攻击敌人.")

    def back(self):
        print(f"{self.name}正在回城.")

jian_hao = Hero(900, "疾风剑豪", 0, 98, 340)
tedamir =Hero(800,"蛮族之王",0,108,345)
print(f"我是{jian_hao.name},血量是{jian_hao.hp},攻击力是{jian_hao.damage}点,移速是{jian_hao.speed}")
jian_hao.dancing()
jian_hao.attack(tedamir)
jian_hao.remove()
jian_hao.back()
