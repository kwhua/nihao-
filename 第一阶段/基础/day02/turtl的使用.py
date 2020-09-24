''
# 1,导入模块
import turtle
# 创建画布
turtle.screensize(800,600)
# 前进命令(默认运动方向向右)
# 改变指针的运动的方向 right left
# turtle.right()
# turtle.left(90)

# 画笔的颜色
turtle.pencolor('yellow')

# 画笔的宽度
turtle.pensize(3)

# 画笔的抬起动作:turtle.penup
turtle.penup()
# 画笔落下动作:turtle.pendown()
turtle.pendown()
# 画笔的速度
turtle.delay(100)
# 填充颜色"默认黑色"
turtle.fillcolor("pink")
turtle.begin_fill()
# 隐藏画笔
turtle.heading()
# 写字
turtle.write('正方形',align="center",font=('繁体','12'))
for x in range(4):
    turtle.left(90)
    turtle.forward(200)
# 取消填充
turtle.end_fill()

# 画圆
# turtle.circle(10,1,360)
# for x in range(360):
#     nextpoint=(100*math.sin())

# 画五角星
turtle.fillcolor('red')
turtle.begin_fill()
for x in range(5):
    turtle.forward(200)
    turtle.right(180-36)

turtle.end_fill()
# 保存画布
turtle.done()









