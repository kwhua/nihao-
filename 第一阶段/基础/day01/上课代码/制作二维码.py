# 下载模块  MyQr

# 导入模块
from MyQR import myqr

# 制作过程

# 使用 myqr 下的run方法制作

myqr.run(
    words='https://u.wechat.com/MC_D0Vb2Mfsg9csmm4lEo3E',  # 扫码展示的内容
    picture='timg.gif', #   背景图片
    colorized=True, #  让背景色变为彩色
    save_name= "笑脸.gif",     # 二维码文件的名字
)

# 微信二维码变成自己制作的二维码
# 草料二维码
# 更多工具
# 上传二维码
# 生成网页连接
# 让words参数等于连接



