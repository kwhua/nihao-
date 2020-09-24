import random

import pygame

# 初始化pygame库，让计算机硬件准备
pygame.init()
# 创建窗口
window = pygame.display.set_mode((1200, 660))
Window_H = 660
Window_W = 1200


class Tank:
    """描述坦克的类"""

    # 血量 方向 图片 移速 坐标
    def __init__(self, x, y):
        # 坦克的血量
        self.hp = 1
        # 坦克的图片
        self.images = {
            "U": pygame.image.load(".\images\p1tankU.gif"),
            "D": pygame.image.load(".\images\p1tankD.gif"),
            "L": pygame.image.load(".\images\p1tankL.gif"),
            "R": pygame.image.load(".\images\p1tankR.gif")
        }
        # 坦克的初始方向
        self.direction = "U"
        # 获取与坦克方向相同的图片
        self.image = self.images[self.direction]
        # 获取图片的位置信息
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # 床键子弹列表
        self.bullet_list = []

    def move(self):
        if self.direction == "U":
            if self.rect.y > 0:
                self.rect.y -= self.speed
            else:
                self.rect.y = 0
        elif self.direction == "D":
            if self.rect.y < Window_H - self.rect.height:
                self.rect.y += self.speed

        elif self.direction == "L":
            if self.rect.x > 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = 0
        elif self.direction == "R":
            if self.rect.x < Window_W - self.rect.width:
                self.rect.x += self.speed

    def fire(self):
        """开火"""

        bullet = Bullet(self)  # 创建子弹对象
        self.bullet_list.append(bullet)  # 将子弹加入子弹列表中


class HeroTank(Tank):
    """我方坦克"""

    def __init__(self, x, y):
        # 继承地方坦克的属性
        super().__init__(x, y)
        # 重写血量属性
        self.hp = 10
        # 我方坦克的速度
        self.speed = 4

    def move(self):
        # 获取键盘按下的按钮事件
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.direction = "L"
            self.image = self.images[self.direction]
            super().move()
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.direction = "R"
            self.image = self.images[self.direction]
            super().move()
        elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            self.direction = "D"
            self.image = self.images[self.direction]
            super().move()
        elif pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            self.direction = "U"
            self.image = self.images[self.direction]
            super().move()


class EnemyTank(Tank):
    """敌方坦克"""

    def __init__(self, x, y):
        # 继承坦克的属性
        super().__init__(x, y)
        # 加载随机敌方坦克样式的图片
        x = random.randint(1, 3)
        self.images = {
            "U": pygame.image.load(f"./images/enemy{x}U.gif"),
            "D": pygame.image.load(f"./images/enemy{x}D.gif"),
            "R": pygame.image.load(f"./images/enemy{x}R.gif"),
            "L": pygame.image.load(f"./images/enemy{x}L.gif")
        }
        # 方向
        self.image = self.images[self.direction]
        # 随机速度
        self.speed = random.randint(1, 3)

    def random_direction(self):
        """增加随机方向的方法"""
        return random.choice(["U", "R", "L", "D"])


    def fire(self):
        """随机敌方坦克出子弹的速率"""
        x = random.randint(1,100)
        if x == 10 :
            super().fire()


class Bullet:
    # （1）子弹类
    # - 属性：位置，图片，速度
    #
    # - 方法：移动
    def __init__(self, tank):
        # 图片
        self.image = pygame.image.load('images/enemymissile.gif')
        # 方向
        self.direction = tank.direction
        # 子弹的速度
        self.speed = 6
        # 设置子弹的位置
        self.rect = self.image.get_rect()
        self.rect.centerx = tank.rect.centerx
        self.rect.centery = tank.rect.centery
        # 设置子弹的状态
        self.is_alive = True

    def move(self):
        """子弹移动"""

        if self.direction == "U":
            if self.rect.centery > -self.rect.height:
                self.rect.centery -= self.speed
            else:
                self.is_alive = False
        elif self.direction == 'D':
            if self.rect.centery < Window_H:
                self.rect.centery += self.speed
            else :
                self.is_alive = False
        elif self.direction == 'L':
            if self.rect.centerx > -self.rect.height:
                self.rect.centerx -= self.speed
            else:
                self.is_alive = False
        elif self.direction == 'R':
            if self.rect.centerx < Window_W:
                self.rect.centerx += self.speed
            else:
                self.is_alive = False


class Game:

    def __init__(self):
        """加载各种属性"""

        # 设置窗口标题
        pygame.display.set_caption("坦克大战")
        # 加载图片文件，返回图片对象
        self.image = pygame.image.load("./images/bg2.jpg")
        # 设置logo
        logo_img = pygame.image.load("./images/eagle.png")
        pygame.display.set_icon(logo_img)
        # 加载我们坦克
        self.hero_tank = HeroTank(600, 600)
        # 加载敌方坦克
        # 生成敌方坦克的列表
        self.ememy_tank_list = []
        # 初始化敌方坦克
        for i in range(5):
            # 随机坐标
            e_tank = EnemyTank(random.randint(1, Window_W), 0)
            self.ememy_tank_list.append(e_tank)



    def draw(self):
        """贴图"""
        # 贴背景图
        window.blit(self.image, (0, 0))
        # 贴我方坦克图


        # 贴坦克图
        window.blit(self.hero_tank.image, (self.hero_tank.rect.x, self.hero_tank.rect.y))
        # 贴敌方坦克
        for e_tank in self.ememy_tank_list:
            x = random.randint(1, 10)
            # 控制速率
            if x == 1:
                e_tank.direction = e_tank.random_direction()

                e_tank.image = e_tank.images[e_tank.direction]
            # 贴敌方坦克
            window.blit(e_tank.image, (e_tank.rect.x, e_tank.rect.y))

            # 敌方坦克射击的方法
            e_tank.fire()

            # 贴敌方子弹图
            for bullet in e_tank.bullet_list:
                if bullet.is_alive:
                    window.blit(bullet.image, (bullet.rect.centerx, bullet.rect.centery))
                else:
                    # 子弹飞出边界,删除子弹
                    e_tank.bullet_list.remove(bullet)
        # 贴我方子弹图
        for bullet in self.hero_tank.bullet_list:
            if bullet.is_alive:
                window.blit(bullet.image, (bullet.rect.centerx, bullet.rect.centery))
            else:
                self.hero_tank.bullet_list.remove(bullet)


    def move(self):
        """我方坦克移动"""
        self.hero_tank.move()
        # 敌方坦克移动
        for e_tank in self.ememy_tank_list:
            e_tank.move()
            # 敌方子弹移动
            for bullet in e_tank.bullet_list:
                bullet.move()
        # 我方子弹移动
        for hero_bullet in self.hero_tank.bullet_list:
            hero_bullet.move()



    def event(self):
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                exit()  # 关闭程序
            # pygame.quit()  # 退出pygame，清理pygame占用资源

            # 2. 键盘按下事件
            if event.type == pygame.KEYDOWN:
                # 判断用户按键

                if event.key == pygame.K_SPACE:
                    # 设计事件
                    self.hero_tank.fire()

    @staticmethod
    def update():
        """刷新界面"""
        pygame.display.update()

    def run(self):
        while True:
            # for event in pygame.event.get():
            #     if event == "j":
            # 调用贴图方法
            self.draw()
            # 增加调用方法
            self.move()
            # 添加事件监听
            self.event()
            # 添加子弹的运动

            # 调用刷新方法
            Game.update()
            print(len(self.hero_tank.bullet_list))


if __name__ == '__main__':
    tan_ke = Game()
    tan_ke.run()
