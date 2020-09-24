import pygame

# 初始化pygame库，让计算机硬件准备
pygame.init()
# 创建窗口
window = pygame.display.set_mode((1200,660))

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

    def draw(self):
        """贴图"""
        # 贴背景图
        window.blit(self.image, (0, 0))


    @staticmethod
    def update():
        """刷新界面"""
        pygame.display.update()


    def run(self):
        while True:
            # 调用贴图方法
            self.draw()
            # 调用刷新方法
            Game.update()


tan_ke = Game()
tan_ke.run()


