#功能实现游戏主窗口
import pygame,time,random#导入模块
_display = pygame.display#赋值给一个变量 调用时方便
color_red = pygame.Color(255,0,0)#同上 v
class MainGame(object):
    screen_width = 900#游戏界面宽度
    screen_height = 550#界面的高度
    Tank_p1 = None#坦克对象
    window = None #窗口对象
    EnemyTank_list = []# 存储所有敌方坦克
    EnemTank_count = 10# 要创建的敌方坦克的数量
    Bullet_list = [] #创建我方子弹列表
    EnemyTank_bullet_list = []
    Explode_list= []
    wall_list = []
    def startGame(self):
        pygame.display.init()#初始化游戏模块的显示
        MainGame.window = _display.set_mode([MainGame.screen_width,MainGame.screen_height])#生成并加载游戏窗口、\
        #pygame.display模块及set_mode方法和pygame相关方法调用设置
        # 见<<https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>> UC浏览器实现自动翻译
        pygame.display.set_caption("坦克大战v1.0")#s设置游戏标题
        self.creatEnemyTank()#类中调用初始敌方坦克方法
        self.creatMyTank()#创建我方坦克
        self.creatWalls()#创建障碍物

        while True:#无限循环 所有行为方法都要无限制的显示
            MainGame.window.fill(pygame.Color(0,0,0))#窗口颜色设置 Window在开始方法已设置为游戏窗口
            self.getEvent()#死循环中 获取事件的值 对其进行相应处理
            MainGame.window.blit(self.drawText("剩余敌方数量%d" %len(MainGame.EnemyTank_list)),(7, 7))#循环游戏窗口加载文本 bilt方法在页面写入另一个

            self.blitWalls()
            if MainGame.Tank_p1 and MainGame.Tank_p1.alive:
                MainGame.Tank_p1.displayTank()#循环调用生成的坦克对象(显示)方法


            self.blitEnemyTank()# 此类中用self 循环展示敌方坦克

            if MainGame.Tank_p1 and not MainGame.Tank_p1.stop:
                MainGame.Tank_p1.move()# 移动
                MainGame.Tank_p1.hitWall()#撞击墙壁
                MainGame.Tank_p1.hitEnemyTank()#撞击敌方坦克方法
                self.blitEnemyBullet()#显示敌方坦克子弹
                self.blitBullet()#显示炮弹
                self.blitExplode()#显示爆炸效果
                time.sleep(0.02)
                _display.update()#获取更新
                #将带有文字的surface 绘制到窗口中 循环
    # 创建敌方坦克

    def creatEnemyTank(self):#创建敌方坦克

        top = 100

        for i in range(MainGame.EnemTank_count):#MainGame.EnemTank_count=5 五次循环创建敌方坦克
            speed = random.randint(3, 6) # 随机模块 random.randint
            # 每次都随机生成一个left值
            left = random.randint(1, 7)
            eTank = EnemyTank(left * 100, top, speed)#生成敌方坦克类对象 传入参数 left为随机
            MainGame.EnemyTank_list.append(eTank)#将创建的每一个敌方坦克添加到列表
    # 将坦克加入到窗口中
    def creatMyTank(self):
        MainGame.Tank_p1 = MyTank(400, 480) # 生成一个坦克类的实例对象
        music = Music("img/start.wav")
        music.play()
    def creatWalls(self):
        for i in range(1,10):
            wall = Wall(60*i,250)
            MainGame.wall_list.append(wall)
    def blitWalls(self):
        for wall in MainGame.wall_list:
            if wall.live == True:
                wall.displayWall()
            else:
                MainGame.wall_list.remove(wall)
    def blitEnemyTank(self):#显示敌方坦克 若出现坦克图片重叠也是符合逻辑
        for eTank in MainGame.EnemyTank_list:
            if eTank.live :
                eTank.displayTank()#将列表中每一个进行显示 eTank为敌方坦克类对象 调用父类Tank类中显示方法
                eTank.randMove()
                eTank.hitWall()
                eTank.hitMyTank()
                ebullet = eTank.shot()

            if ebullet:#如果不为空
                MainGame.EnemyTank_bullet_list.append(ebullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)
    def blitEnemyBullet(self):#将敌方坦克加入到窗口中
        for ebullet in MainGame.EnemyTank_bullet_list:
            if ebullet.alive:
                ebullet.display_bullet()
                ebullet.bulletMove()
                ebullet.hitWalls()
            if MainGame.Tank_p1.alive:
                ebullet.hitMyTank()
            else:
                MainGame.EnemyTank_bullet_list.remove(ebullet)
    def blitBullet(self):#显示子弹
        for bullet in MainGame.Bullet_list:#事件中获的子弹的列表进行遍历 类似显示坦克方法 逐个展示
            if bullet.alive:#Bullet类中设置的标签 来判断子弹的存活 True为生 根据炮弹移动方法bulletmove()中所加限制条件
                bullet.display_bullet()#调用列表中子弹对象的显示方法
                bullet.bulletMove()#子弹的移动
                bullet.hitEnemyTank()#调用与敌方坦克的碰撞检测方法
                bullet.hitWalls()#d调用子弹碰撞墙壁
            else:

                MainGame.Bullet_list.remove(bullet)#如果为False bulletmove()中触碰墙壁就是False 就从列表删除 循环执行
    def blitExplode(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.display_explode()
                music = Music("img/blast.wav")
                music.play()
            else:
                MainGame.Explode_list.remove(explode)
    def drawText(self,content):#文本 写入游戏窗口
        pygame.font.init()#初始化字体
        font = pygame.font.SysFont("kaiti",18)#创建字体对象
        text_sf = font.render(content,True,color_red)#字体样式对象
        return text_sf #返回内容的surface
    def getEvent(self):#获取所有事件
        eventlist = pygame.event.get()#所有事件列表
        for event in eventlist:#遍历每一个事件进行判断 键盘输入的字符
        #type属性
            if event.type == pygame.QUIT:#如果是QUIT(就是点击窗口的退出按钮 叉号)
                print("退出游戏")
            self.gameOver()#退出方法
            if event.type == pygame.KEYUP:#如果键盘按钮抬起 并且是上下左右键
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP \
                        or event.key == pygame.K_DOWN:
                    if MainGame.Tank_p1 and MainGame.Tank_p1.alive:
                        MainGame.Tank_p1.stop = True#stop为True 按钮抬起就停止 start方法中的开关 实现坦克按住按钮持续移动

            if event.type == pygame.KEYDOWN:#如果事件的类型为按下按键进行如下判断
                if event.key == pygame.K_ESCAPE :
                    self.creatMyTank()
            if MainGame.Tank_p1 and MainGame.Tank_p1.alive:
                if event.key == pygame.K_LEFT:#如果为左方向键 如下为同一类型
                    print("向左移动")
                MainGame.Tank_p1.direction = "L"#设置坦克方向进行判断向左就是L，
                # 并设置游戏窗口的界限 还可以利用方向作为字典的键获取坦克图片 坦克的移动方向
                #就是加载不同方向的坦克图片 呈现出移动的效果
                MainGame.Tank_p1.stop = False#坦克移动的开关 循环使用 False为移动
                if event.key == pygame.K_RIGHT:
                    print("向右移动")
                MainGame.Tank_p1.direction = "R"
                MainGame.Tank_p1.stop = False
                if event.key ==pygame.K_UP:
                    print("向上移动")
                MainGame.Tank_p1.direction = "U"
                MainGame.Tank_p1.stop = False
                if event.key == pygame.K_DOWN:
                    print("向下移动")
                MainGame.Tank_p1.direction = "D"
                MainGame.Tank_p1.stop = False
                if event.key == pygame.K_SPACE:#空格键发射子弹
                    if len(MainGame.Bullet_list) < 3:#控制子弹在屏幕显示的数量 太多没有游戏体验 列表中存储三个
                        m = Bullet(MainGame.Tank_p1)#子弹类对象 添加到列表 开始方法调用显示子弹 子弹触碰墙壁列表内移除对象
                        MainGame.Bullet_list.append(m)
                        music =Music("img/fire.wav")
                        music.play()
    def gameOver(self):#游戏结束方法
        exit()
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Tank(BaseItem):#坦克的父类
    def __init__(self,left,top):
    #坦克图片集合
    self.images = {"U":pygame.image.load("img/p1tankU.gif"),
                   "D": pygame.image.load("img/p1tankD.gif"),
                   "L":pygame.image.load("img/p1tankL.gif"),
                   "R": pygame.image.load("img/p1tankR.gif"),}#坦克各方向图片的加载
    #坦克的方向
    self.direction = "U"
    #坦克初始化时候的默认图片，根据坦克的方向从字典里去提取
    self.image = self.images[self.direction]
    #坦克的区域（left,top,width,height）坦克位置以及坦克的大小
    self.rect = self.image.get_rect()
    self.rect.left = left#坦克距离左边位置修改默认参数指定的位置
    self.rect.top = top#将坦克距离上边的位置修改我指定的位置
    self.speed = 15#设置坦克的速度
    self.stop = True #设置移动的开关
    self.oldtop = self.rect.top
    self.oldleft = self.rect.left
    def move(self):
        self.oldtop = self.rect.top
    self.oldleft = self.rect.left
    if self.direction == "U":#向上时
        if self.rect.top > 0:#self.rect = self.image.get_rect()
        # self.rect.top = top#将坦克距离上边的位置修改我指定的位置
        self.rect.top -= self.speed#坦克的速度距离每一次调用时相减 直到<0时
    elif self.direction == "D":#向下时
        if self.rect.top < MainGame.screen_height-MainGame.Tank_p1.rect.height:#下边界小于窗口的高度减去坦克自身的高度的距离
            self.rect.top += self.speed #距离加速度的距离 循环一次添加一次
    elif self.direction == "L":
        if self.rect.left > 0:
            self.rect.left -= self.speed
    elif self.direction == "R":
        if self.rect.left < MainGame.screen_width -MainGame.Tank_p1.rect.width:
            self.rect.left += self.speed
    def stay(self):
        self.rect.left = self.oldleft
    self.rect.top = self.oldtop
    def hitWall(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.stay()
    def shot(self):
        return Bullet(self)
    def displayTank(self):#坦克显示方法
    #1.重新设置坦克的图片
    self.image = self.images[self.direction]
    #2.将坦克加入到窗口中
    MainGame.window.blit(self.image,self.rect)#调用MainGame window方法
    # 传入图片和位置 self.rect = self.image.get_rect()
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)
    def hitEnemyTank(self):
        for etank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(etank,self):
                self.stay()
class EnemyTank(Tank):#敌方坦克类
    def __init__(self,left,top,speed):#初始化敌方坦克 三个参数
        self.images = {"U": pygame.image.load("img/enemy1U.gif"),
                       "D": pygame.image.load("img/enemy1D.gif"),
                       "L": pygame.image.load("img/enemy1L.gif"),
                       "R": pygame.image.load("img/enemy1R.gif"), }#加载敌方坦克图片
    # 坦克的方向
    self.direction = self.randDirection()#自定义坦克的随机方向
    self.image = self.images[self.direction]#坦克的信息 从字典中以键获得值
    # 坦克所在的区域 Rect->
    self.rect = self.image.get_rect()#获得坦克图片的距离 距左和距上
    # 指定坦克初始化位置 分别距x，y轴的位置
    self.rect.left = left#距左的位置>>形参
    self.rect.top = top#距上的位置
    # 新增速度属性
    self.speed = speed #速度>>初始化时设置
    self.stop = True
    self.step = 50#设置步数
    self.live = True
    def randDirection(self):#随机生成敌方坦克的方向图片
        num = random.randint(1, 4)
    if num == 1:
        return 'U'
    elif num == 2:
        return 'D'
    elif num == 3:
        return 'L'
    elif num == 4:
        return 'R'
    def randMove(self):#敌方坦克随机移动
        if self.step <= 0:#如果步数为0
            self.direction = self.randDirection()#方向为随机方向
            self.step = 30# 重置步数
        else:
            self.move()#移动 坦克位置不断改变
            self.step -= 1#步数每次循环减一
    def shot(self):
        s = random.randint(1,1000)
    if s <30:
        return Bullet(self)
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.Tank_p1):
            self.stay()
class Bullet(BaseItem):#炮弹类
    def __init__(self,tank):
        self.image = pygame.image.load("img\enemymissile.gif")
    self.direction = tank.direction
    #子弹速度
    self.speed = 18
    self.rect = self.image.get_rect()#获得子弹的对象的坐标 只计算距离左侧和和上面
    #子弹初始化位置要根据坦克大方向进行调整 可以自己画图计算
    if self.direction == "U":
        #子弹的位置 left += 坦克宽度的一半 - 子弹的宽度的一半
        self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
        self.rect.top = tank.rect.top - self.rect.height
    elif self.direction == "D":
        self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
        self.rect.top = tank.rect.top - self.rect.height
    elif self.direction == "L":
        self.rect.left = tank.rect.left - tank.rect.width / 2 - self.rect.width / 2
        self.rect.top = tank.rect.top + tank.rect.width/2 -self.rect.width/2
    elif self.direction == "R":
        self.rect.left = tank.rect.left + tank.rect.width / 2
        self.rect.top = tank.rect.top + tank.rect.width/2 -self.rect.width/2
    speed = 10#速度
    alive = True#设置一个小标签 作判断
    def bulletMove(self):#炮弹移动
        if self.direction == "U":
            if self.rect.top > 0 :#距离限制计算 self子弹对象本身 rect.top距离窗口上方 rect.left左侧
                self.rect.top -= self.speed
            else:
            self.alive = False#此为<0时的情况 同下都是触碰墙壁时的情况
        elif self.direction == "D":
            if self.rect.top < MainGame.screen_height - self.rect.height:#屏幕高度 - 子弹的高度
                self.rect.top += self.speed
            else:
            self.alive = False
        elif self.direction == "L":
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
            self.alive = False
        elif self.direction == "R":
            if self.rect.left < MainGame.screen_width - self.rect.width:
                self.rect.left += self.speed
            else:
            self.alive = False
    def hitEnemyTank(self):#我方子弹与敌方坦克相碰
        for etank in MainGame.EnemyTank_list:#敌方坦克列表
            if pygame.sprite.collide_rect(etank,self):#sprite中的相撞测试
                explode = Explode(etank)#产生一个爆炸效果
            MainGame.Explode_list.append(explode)
            self.alive = False
            etank.live = False
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.Tank_p1):
            explode = Explode(MainGame.Tank_p1)
            MainGame.Explode_list.append(explode)
            MainGame.Tank_p1.alive = False
            self.alive = False
    def hitWalls(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.alive = False
            wall.hp -= 1
            if wall.hp <= 0:
                wall.live = False
    def display_bullet(self):#显示子弹方法
        MainGame.window.blit(self.image,self.rect)#窗口写入
class Explode:#爆炸效果
    def __init__(self,tank):
        self.step = 0
    self.rect = tank.rect
    self.images = [pygame.image.load("img/blast0.gif"),
                   pygame.image.load("img/blast1.gif"),
                   pygame.image.load("img/blast2.gif"),
                   pygame.image.load("img/blast3.gif"),
                   pygame.image.load("img/blast4.gif"),
                   pygame.image.load("img/blast5.gif"),
                   pygame.image.load("img/blast6.gif"),
                   pygame.image.load("img/blast7.gif"),]
    self.live = True
    self.image = self.images[self.step]
    def display_explode(self):#显示爆炸效果
        if self.step < len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0
class Wall:
    def __init__(self,left,top):
        self.image = pygame.image.load("img/steels.gif")
    self.rect = self.image.get_rect()

    self.rect.left = left
    self.rect.top = top
    self.live = True
    self.hp = 3
    def displayWall(self):#显示障碍物
        MainGame.window.blit(self.image,self.rect)

class Music:#音效
    def __init__(self,filename):
        self.filename = filename
    pygame.mixer.init()#混合器的初始
    pygame.mixer.music.load(self.filename)#加载音乐文件
    def play(self):
        pygame.mixer.music.play(loops=0)#播放音乐

MainGame().startGame()