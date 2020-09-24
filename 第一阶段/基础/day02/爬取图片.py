'''
网络请求模块 requests  urllib
图片的地址
'''

'下载模块'


'''
get方法
'''

# 1,使用requests模块
import requests

# 2,图片地址:https://game.gtimg.cn/images/lol/act/img/skin/big40000.jpg
# 请求方法: get


# 请求地址   获取地址内容(响应)
# 后面的.content是获取地址的内容
'''
查看页面的二进制数据
'''
img=requests.get("https://game.gtimg.cn/images/lol/act/img/skin/big40000.jpg").content
print(img)

# 保存图片
with open('迦娜.jpg','wb') as f:
    f.write(img)


import requests
try:
    for x in range(1,24):
        img1 = requests.get(f"https://game.gtimg.cn/images/lol/act/img/skin/big4000{x}.jpg").content
        print(img1)
        with open(f'迦娜{x}.jpg','wb') as f:
           f.write(img1)
except:
    print("")

import requests
try:
    for x in range(1,251):
        img2=requests.get(f"http://pic.netbian.com/uploads/allimg/200825/000249-15982849691625.jpg").content
        print(img2)
        with open(f"图片{x}","wb") as f:
            f.write(img2)
except:
    print()