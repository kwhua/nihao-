"""
分析
    坦克
        属性:血量(hp),图片(image),方向(direction),速度(speed),坐标(x,y)
        方法:移动(move),开火(fire)
"""
import pygame
# 初始化
pygame.init()

# 创建窗口
window = pygame.display.set_mode((1200,660))


class Tank:
    def __init__(self,x,y):
        self.hp = 1  # 血量
        self.speed = 10
        self.images = {
            "U":pygame.image.load('images/p1tankU.gif'),
            "D":pygame.image.load('images/p1tankD.gif'),
            "L":pygame.image.load('images/p1tankL.gif'),
            'R':pygame.image.load('images/p1tankR.gif')
        }

        self.direction = "D"  # 初始方法
        # 坦克的图片
        self.image = self.images[self.direction]

        # 获取图片的rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def move(self):
        """坦克移动"""
        # todo 逻辑需要完善:坦克移出边界

        if self.direction == "U":
            self.rect.y -= self.speed
        elif self.direction == "D":
            self.rect.y += self.speed
        elif self.direction == "L":
            self.rect.x -= self.speed
        elif self.direction == "R":
            self.rect.x += self.speed



    def fire(self):
        """开火"""
        # todo 开火
        pass





class Game:
    """加载各种元素,实现各种元素之间的交互"""

    def __init__(self):
        """初始化方法"""
        # 加载背景图
        self.bg = pygame.image.load('./images/bg3.jpg')
        # 设置窗口标题
        pygame.display.set_caption("坦克大战")
        # 设置logo
        logo_img = pygame.image.load('images/enemy1D.gif')
        pygame.display.set_icon(logo_img)

        # 加载坦克
        self.tank = Tank(800,200)


    def draw(self):
        """贴图"""
        # 贴背景图
        window.blit(self.bg,(0,0))
        # 贴坦克图
        window.blit(self.tank.image,(self.tank.rect.x,self.tank.rect.y))


    def move(self):
        """各种元素的移动"""
        # 坦克移动
        self.tank.move()

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
            # 刷新
            self.update()




if __name__ == '__main__':
    # 启动游戏
    game = Game()
    game.run()




