# 在学习过程中有什么不懂得可以加我的
# python学习交流扣扣qun，784758214
# 群里有不错的学习视频教程、开发工具与电子书籍。
# 与你分享python企业当下人才需求及怎么从零基础学习好python，和学习什么内容
import re,requests

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971"
response = requests.get(url,verify=False)
#将车站的名字和编码进行提取
chezhan = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
chezhan_code = dict(chezhan)

chezhan_names = dict(zip(chezhan_code.values(),chezhan_code.keys()))
#print(chezhan_names)

