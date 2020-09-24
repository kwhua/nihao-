import time
from time import strftime,gmtime

print(strftime("%m/%d/%Y %H:%M"))
print(strftime("%Y/%d/%m %H:%M"))
'07/21/2016 19:57'
print(time.strftime("%Y%m%d"))
'20160721'
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
'2016-07-21 11:47:51'
from datetime import datetime

print(str(datetime.now()))