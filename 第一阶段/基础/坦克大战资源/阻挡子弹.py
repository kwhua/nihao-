import random

import pygame

# 初始化pygame库，让计算机硬件准备
pygame.init()
# 创建窗口
window = pygame.display.set_mode((1200, 660))
Window_H = 660
Window_W = 1200
Tank_Count = 5  # 生成敌方坦克的数量
Obstacle_count = 100  # 生成障碍物的数量


class Tank:
    """描述坦克的类"""

    # 血量 方向 图片 移速 坐标
    def __init__(self, x, y):
        # 坦克的血量
        self.hp = 1
        # 坦克的速度
        self.speed = 4
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

        # 创建子弹列表
        self.bullet_list = []

        # 记录旧坐标
        self.oldx = self.rect.x
        self.oldy = self.rect.y

        # 增加坦克的状态
        self.is_alive = True

    def move(self):
        # 每次移动都要记录目标
        self.oldx = self.rect.x
        self.oldy = self.rect.y

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

    def back(self):
        """遇到墙之后回到旧坐标"""
        self.rect.x = self.oldx
        self.rect.y = self.oldy


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
        x = random.randint(1, 100)
        if x < 3:
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

        # 子弹的伤害
        self.damage = 5

        # 子弹的速度
        self.speed = 6

        # 设置子弹的位置
        # 获取子弹的位置信息
        self.rect = self.image.get_rect()

        # 记录子弹的位置
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
            else:
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

    def hit_enemy(self, enemy):
        """击中敌方坦克"""
        if pygame.Rect.colliderect(self.rect, enemy.rect):
            self.is_alive = False
            enemy.hp -= self.damage
            if enemy.hp == 0:
                enemy.is_alive = False


class Obstacle:
    """障碍的类"""

    # 血量 坐标  图片
    def __init__(self, x, y, type_):
        self.hp = 10000000000000
        self.image = pygame.image.load(f"./images/{type_}.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #     新增墙的状态
        self.is_alive = True

    def block_item(self, item):
        #     """
        #        阻挡对象：子弹或是坦克
        #        检测碰撞：使用pygame提供的pygame.Rect.colliderect(rect1, rect2)，返回布尔值
        #    """

        if pygame.Rect.colliderect(self.rect, item.rect):
            if isinstance(item, Tank):
                return True

            if isinstance(item, Bullet):
                """检查子弹"""
                # 修改子弹的状态
                item.is_alive = False
                self.hp -= item.damage
                if self.hp <= 0:
                    self.is_alive = False


class Brick(Obstacle):
    """砖墙"""

    def __init__(self, x, y):
        # 继承父类的属性
        super().__init__(x, y, "walls")
        self.hp = 10


class Stone(Obstacle):
    """石头墙"""

    def __init__(self, x, y):
        super().__init__(x, y, "steels")
        # self.image = pygame.image.load("images\steels.gif")


class WaterWall(Obstacle):
    """水墙"""

    def __init__(self, x, y):
        super().__init__(x, y, "water")
        # self.image = pygame.image.load("images\water.gif")

    def block_item(self, item):
        #     """
        #        阻挡对象：子弹或是坦克
        #        检测碰撞：使用pygame提供的pygame.Rect.colliderect(rect1, rect2)，返回布尔值
        #    """

        if pygame.Rect.colliderect(self.rect, item.rect):
            if isinstance(item, Tank):
                return True

            if isinstance(item, Bullet):
                """检查子弹"""
                # 修改子弹的状态
                item.is_alive = True



class Game:

    def __init__(self):
        """加载各种属性"""

        # 设置窗口标题
        pygame.display.set_caption("坦克大战")

        # 加载图片文件，返回图片对象
        self.image = pygame.image.load("./images/blank.jpg")

        # 设置logo
        logo_img = pygame.image.load("./images/eagle.png")
        pygame.display.set_icon(logo_img)

        # 加载我方坦克
        self.hero_tank = HeroTank(600, 600)

        # 加载敌方坦克
        # 生成敌方坦克的列表
        self.ememy_tank_list = []
        # 初始化敌方坦克
        for i in range(Tank_Count):
            # 随机坐标
            e_tank = EnemyTank(random.randint(1, Window_W), 0)
            self.ememy_tank_list.append(e_tank)

        # 增加墙障碍
        self.obstacle_list = []  # 生成墙列表
        # 产生随机个障碍
        for x in range(Obstacle_count):
            if x % 2 == 0:  # 产生砖墙
                brick = Brick(random.randrange(0, 1140, 60), random.randrange(60, 600, 60))
                self.obstacle_list.append(brick)
            elif x % 3 == 0:  # 石头墙
                stone = Stone(random.randrange(0, 1140, 60), random.randrange(60, 600, 60))
                self.obstacle_list.append(stone)
            else:  # 水墙
                water = WaterWall(random.randrange(0, 1140, 60), random.randrange(60, 600, 60))
                self.obstacle_list.append(water)

    def draw(self):
        """贴图"""
        # 贴背景图
        window.blit(self.image, (0, 0))
        # 贴障碍物图及碰撞检测
        for obstacle in self.obstacle_list:
            # 判断墙的状态
            if obstacle.is_alive:
                # 如果墙存在,则把墙贴上
                window.blit(obstacle.image, (obstacle.rect.x, obstacle.rect.y))
            else:
                # 墙不在则将墙移除
                self.obstacle_list.remove(obstacle)
            # 和我方坦克进行检测
            if obstacle.block_item(self.hero_tank):
                self.hero_tank.back()  # 将我方法坦克的坐标还原

            # 和我方的子弹进行检验
            for bullet in self.hero_tank.bullet_list:
                obstacle.block_item(bullet)

            # 和敌方坦克进行检测
            for e_tank in self.ememy_tank_list:
                if obstacle.block_item(e_tank):
                    e_tank.back()  # 恢复敌方坦克的坐标
                # 和敌方的子弹检测
                for bullet in e_tank.bullet_list:
                    obstacle.block_item(bullet)

        # 贴我方坦克图
        window.blit(self.hero_tank.image, (self.hero_tank.rect.x, self.hero_tank.rect.y))
        # 贴我方子弹图
        for bullet in self.hero_tank.bullet_list:
            # 判断子弹的状态
            if bullet.is_alive:
                # 存在,贴我方子弹图
                window.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
            else:
                # 不存在删除子弹
                self.hero_tank.bullet_list.remove(bullet)

        # 贴敌方坦克
        for e_tank in self.ememy_tank_list:
            if e_tank.is_alive:
                # 设置坦克的随机方向
                x = random.randint(1, 100)
                if x == 10:
                    # 随机坦克的方向
                    e_tank.direction = e_tank.random_direction()
                    # 获取坦克的最新方向的图片
                    e_tank.image = e_tank.images[e_tank.direction]
                #     贴敌方坦克图
                window.blit(e_tank.image, (e_tank.rect.x, e_tank.rect.y))
            else:
                self.ememy_tank_list.remove(e_tank)

            # 敌方坦克发射图片
            e_tank.fire()

            # 贴敌方子弹图
            for bullet in e_tank.bullet_list:
                # 判断子弹的状态
                if bullet.is_alive:
                    # 贴子弹图
                    window.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
                # 如果子弹不存在了,将它在列表中删除
                else:
                    e_tank.bullet_list.remove(bullet)

    def move(self):
        """各种元素的移动"""
        # 我方坦克移动
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

            # 调用贴图方法
            self.draw()

            # 增加调用方法
            self.move()

            # 添加事件监听
            self.event()

            # 调用刷新方法
            Game.update()


if __name__ == '__main__':
    # 启动游戏
    tan_ke = Game()
    tan_ke.run()
