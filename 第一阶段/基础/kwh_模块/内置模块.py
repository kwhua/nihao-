import random
# 1.random模块
# 产生随机数
# 产生随机小数
'小数'
# random.random()  # 0~1之间的小数
# random.uniform(5,10)  # m~n之间的随机小数
# '随机整数'
# random.randint(1,10)  # m~n之间的岁间整数
# random.randrange(1,10,2)  # start 开始,stop结束,step步长)左开右闭
# # choice(lst)  给定列表随机选择一个元素
# lst = [1,23,8,6,23,24,3,2]
# random.choice(lst)
# # shuffle(lst):随机打乱给定的对象
# random.shuffle(lst)

# time
import time

print(time.time())
# sleep 睡眠
time.sleep(5)
print("我已经休息了5秒.")
# time.time()计算机现在的时间(从1970年1月1日开始到现在的时间)
print(time.time())
# localtime([timestamp])将本地时间转换为时间元组
print(time.localtime())
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=10, tm_hour=14, tm_min=40, tm_sec=41, tm_wday=3, tm_yday=254, tm_isdst=0)
print(time.gmtime())
print(time.mktime())


print("-"*50)
from time import strftime,gmtime

print(strftime("%m/%d/%Y %H:%M"))
'07/21/2016 19:57'
print(time.strftime("%Y%m%d"))
'20160721'
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
'2016-07-21 11:47:51'
from datetime import datetime

print(str(datetime.now()))
now_time = time.time()
birthday = time.strptime("1999-01-01 8:00:00","%Y-%m-%d %H:%M:%S")
print(birthday)
birthday_ = time.mktime(birthday)
s = now_time - birthday_
print(s)