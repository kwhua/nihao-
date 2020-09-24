"""
	2 模拟完成cf选手对战游戏，
	（1）需要有玩家类和枪类
	（2）玩家包含：名字，血量等属性，枪包含的名字，伤害等属性
	（3）玩家使用枪支进行互相射击
	（4）使用面向对象方式完成上述过程
"""


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


    def shoot(self,gun):
        print(f"{self.name}拿着{self.gun}和{Player.name}拿着{Gun.name}对射.")

class Gun:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage




tc = Player("tc", 100)
kwh = Player("kwh", 100)

ak_47 = Gun("ak-47", 87)
gatling = Gun("加特林", 80)
s686 = Gun("S686",100)
m4a1 = Gun("M4A1-S",86)

