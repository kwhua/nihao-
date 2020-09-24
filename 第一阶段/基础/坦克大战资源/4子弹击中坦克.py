"""
分析
    障碍物
        属性:血量hp,位置(x,y),图片
        方法:阻挡元素
"""
import random
import time

import pygame

# 初始化
pygame.init()

WINDOW_W = 1200
WINDOW_H = 660

ENEMY_TANK_COUNT = 5
Obstacle_COUNT = 20

# 创建窗口
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))


class Obstacle:
    def __init__(self, x, y, type_):
        """初始化墙属性"""
        self.hp = 1000000  # 障碍物血量,认为无敌
        self.image = pygame.image.load(f"images/{type_}.gif")
        # 获取rectangle属性
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # 新增墙状态
        self.is_alive = True

    def block_item(self, item):
        """阻挡游戏中的元素"""
        if pygame.Rect.colliderect(self.rect, item.rect):
            if isinstance(item, Tank):
                return True
            if isinstance(item, Bullet):
                # 修改子弹状态
                item.is_alive = False
                # 降低墙的血量
                self.hp -= item.damage
                if self.hp <= 0:
                    self.is_alive = False


class Brick(Obstacle):
    """砖墙"""

    def __init__(self, x, y, type_):
        super().__init__(x, y, type_)
        # 修改血量
        self.hp = 20


class Steels(Obstacle):
    pass


class Water(Obstacle):
    pass


class Bullet:
    def __init__(self, tank):
        self.speed = 3
        self.hp = 1
        self.damage = 5
        self.image = pygame.image.load("images/enemymissile.gif")

        # 子弹方向
        self.direction = tank.direction

        # rect属性
        self.rect = self.image.get_rect()
        # 记录子弹的位置
        self.rect.x = tank.rect.centerx
        self.rect.y = tank.rect.centery

        # 子弹状态
        self.is_alive = True

    def move(self):
        """子弹的移动"""
        if self.direction == 'U':
            if self.rect.y > -self.rect.height:
                self.rect.y -= self.speed
            else:
                self.is_alive = False

        elif self.direction == "D":
            if self.rect.y < WINDOW_H:
                self.rect.y += self.speed
            else:
                self.is_alive = False

        elif self.direction == "L":
            if self.rect.x > -self.rect.width:
                self.rect.x -= self.speed
            else:
                self.is_alive = False
        elif self.direction == "R":
            if self.rect.x < WINDOW_W:
                self.rect.x += self.speed
            else:
                self.is_alive = False


class Tank:
    def __init__(self, x, y):
        self.hp = 1  # 血量
        self.speed = 3
        self.images = {
            "U": pygame.image.load('images/p1tankU.gif'),
            "D": pygame.image.load('images/p1tankD.gif'),
            "L": pygame.image.load('images/p1tankL.gif'),
            'R': pygame.image.load('images/p1tankR.gif')
        }

        self.direction = "U"  # 初始方法
        # 坦克的图片
        self.image = self.images[self.direction]

        # 获取图片的rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # 记录子弹列表
        self.bullet_list = []

        # 记录旧坐标
        self.oldx = self.rect.x
        self.oldy = self.rect.y

    def move(self):
        """坦克移动"""

        # 记录旧坐标
        self.oldx = self.rect.x
        self.oldy = self.rect.y

        if self.direction == "U":
            if self.rect.y > 0:
                self.rect.y -= self.speed
        elif self.direction == "D":
            if self.rect.y < WINDOW_H - self.rect.height:
                self.rect.y += self.speed
        elif self.direction == "L":
            if self.rect.x > 0:
                self.rect.x -= self.speed
        elif self.direction == "R":
            if self.rect.x < WINDOW_W - self.rect.width:
                self.rect.x += self.speed

    def fire(self):
        """开火"""
        bullet = Bullet(self)
        self.bullet_list.append(bullet)

    def back(self):
        """遇到墙之后恢复原坐标"""
        self.rect.y = self.oldy
        self.rect.x = self.oldx


class HeroTank(Tank):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hp = 10

    def move(self):
        """自定义移动"""

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.direction = "L"
            self.image = self.images[self.direction]
            super().move()

        elif pressed_keys[pygame.K_RIGHT]:
            self.direction = "R"
            self.image = self.images[self.direction]
            super().move()
        elif pressed_keys[pygame.K_UP]:
            self.direction = "U"
            self.image = self.images[self.direction]
            super().move()
        elif pressed_keys[pygame.K_DOWN]:
            self.direction = "D"
            self.image = self.images[self.direction]
            super().move()


class EnemyTank(Tank):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 1
        x = random.randint(1, 3)  # 随机坦克的样式
        self.images = {
            "U": pygame.image.load(f'images/enemy{x}U.gif'),
            "D": pygame.image.load(f'images/enemy{x}D.gif'),
            "L": pygame.image.load(f'images/enemy{x}L.gif'),
            'R': pygame.image.load(f'images/enemy{x}R.gif')
        }
        # 敌人坦克的图片
        self.image = self.images[self.direction]

    def fire(self):
        x = random.randint(1, 100)
        if x == 10:
            super().fire()

    def random_dirction(self):
        """随机坦克方向"""
        return random.choice(["U", "R", "L", "D"])


class Game:
    """加载各种元素,实现各种元素之间的交互"""

    def __init__(self):
        """初始化方法"""
        # 加载背景图
        self.bg = pygame.image.load('./images/bg2.jpg')
        # 设置窗口标题
        pygame.display.set_caption("坦克大战")
        # 设置logo
        logo_img = pygame.image.load('images/enemy1D.gif')
        pygame.display.set_icon(logo_img)

        # 加载我方坦克
        self.hero_tank = HeroTank(800, 600)

        # 敌方坦克列表
        self.enemy_tank_list = []
        # 加载敌方坦克
        for i in range(ENEMY_TANK_COUNT):  # 创建5辆敌方坦克
            # 随机坐标（默认在第一行出现）
            e_tank = EnemyTank(random.randint(0, 1140), 0)
            self.enemy_tank_list.append(e_tank)

        # 创建障碍物对象
        self.obstacle_list = []  # 障碍物列表
        for i in range(Obstacle_COUNT):
            if i % 5 == 0:
                self.steel = Steels(random.randrange(0, 1200, 60), random.randrange(60, 600, 60),
                                    "steels")
                self.obstacle_list.append(self.steel)
            else:
                self.brick = Brick(random.randrange(0, 1200, 60), random.randrange(60, 600, 60),
                                   "walls")
                self.obstacle_list.append(self.brick)

    def draw(self):
        """贴图"""
        # 贴背景图
        window.blit(self.bg, (0, 0))
        # 贴障碍物图及碰撞检测
        for obstacle in self.obstacle_list:
            # 判断墙状态
            if obstacle.is_alive:
                window.blit(obstacle.image, (obstacle.rect.x, obstacle.rect.y))
            else:
                self.obstacle_list.remove(obstacle)  # 移除消失的墙

            # 和我方坦克检测
            if obstacle.block_item(self.hero_tank):
                self.hero_tank.back()  # 恢复旧坐标

            # 和我方子弹检测碰撞
            for bullet in self.hero_tank.bullet_list:
                obstacle.block_item(bullet)

            # 阻挡敌方坦克
            for e_tank in self.enemy_tank_list:
                if obstacle.block_item(e_tank):
                    e_tank.back()  # 恢复旧坐标
                # 遍历敌方坦克的子弹列表
                for bullet in e_tank.bullet_list:
                    obstacle.block_item(bullet)

        # 贴坦克图
        window.blit(self.hero_tank.image, (self.hero_tank.rect.x, self.hero_tank.rect.y))

        # 贴敌方坦克
        for e_tank in self.enemy_tank_list:
            x = random.randint(1, 100)
            if x < 5:
                # 随机坦克方向
                e_tank.direction = e_tank.random_dirction()
                # 获取最新方向的图片
                e_tank.image = e_tank.images[e_tank.direction]
            # 贴图
            window.blit(e_tank.image, (e_tank.rect.x, e_tank.rect.y))

            # 敌方发射子弹
            e_tank.fire()

            # 贴敌方子弹图
            for bullet in e_tank.bullet_list:
                if bullet.is_alive:
                    window.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
                else:
                    # 飞出边界,删除子弹
                    e_tank.bullet_list.remove(bullet)

        # 贴我方坦克子弹
        for bullet in self.hero_tank.bullet_list:
            if bullet.is_alive:
                window.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
            else:
                # 飞出边界,删除子弹
                self.hero_tank.bullet_list.remove(bullet)

    def move(self):
        """各种元素的移动"""
        # 我方坦克移动
        self.hero_tank.move()
        # 敌方坦克移动
        for e_tank in self.enemy_tank_list:
            e_tank.move()
            # 敌方子弹移动
            for bullet in e_tank.bullet_list:
                bullet.move()

        # 我方子弹移动
        for bullet in self.hero_tank.bullet_list:
            bullet.move()

    def event(self):
        """监听事件"""
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                exit()  # 关闭程序

            # 2. 键盘按下事件
            if event.type == pygame.KEYDOWN:
                # 判断用户按键
                if event.key == pygame.K_SPACE:
                    print("发射子弹")
                    self.hero_tank.fire()

    @staticmethod
    def update():
        """刷新界面"""
        pygame.display.update()

    def run(self):
        """调用类内部各个方法"""
        while True:
            # 贴图
            self.draw()
            # 移动
            self.move()
            # 监听事件
            self.event()
            # 刷新
            self.update()
            print(len(self.hero_tank.bullet_list))


if __name__ == '__main__':
    # 启动游戏
    game = Game()
    game.run()
