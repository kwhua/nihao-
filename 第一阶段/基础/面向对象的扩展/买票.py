from login import Login
import os
import json
import time
from collections import deque, OrderedDict

class Station:
    """ 查询车票信息 """

    def __init__(self):
        # 使用登录时候的session,这样好一些!
        self.session = Login.session
        self.headers = Login.headers


    def station_name_code(self):
        """
        功能:获取每个站点的名字和对应的代码,并保存到本地
        :return: 无
        """
        filename = 'station_name.txt'

        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        resp = self.session.get(url, headers=self.headers)
        if resp.status_code == 200:
            print('station_name_code():获取站点信息成功!')
            with open(filename, 'w') as f:
                for each in resp.text.split('=')[1].split('@'):
                    if each != "'":
                        f.write(each)
                        f.write('\n')
        else:
            print('station_name_code() error! status_code:{}, url: {}'
                  .format(resp.status_code, resp.url))

    def save_station_code(self, filename):
        """
        功能:从站点文件中提取站点与其对应的代码,并保存到文件中
        :return:
        """

        if not os.path.exists(filename):
            print('save_station_code():',filename,'不存在,正在下载!')
            self.station_name_code()

        file = 'name_code.json'
        name_code_dict = {}
        with open(filename, 'r') as f:
            for line in f:
                # 对读取的行都进行split操作,然后提取站点名和其代码
                name = line.split('|')[1] # 站点名字
                code = line.split('|')[2] # 每个站点对应的代码
                # 每个站点肯定都是唯一的
                name_code_dict[name] = code

        # 把name,code保存到本地文件中,方便以后使用
        with open(file, 'w') as f:
            # 不以ascii码编码的方式保存
            json.dump(name_code_dict, f, ensure_ascii=False)


    def query_ticket(self):
        """
        功能:查票操作
        :return: 返回查询到的所有车次信息
        """

        data = self._query_prompt()
        if not data:
            print('query_ticket() error: {}'.format(data))
        _, from_station, to_station = data.keys()
        train_date = data.get('train_date')
        from_station_code = data.get(from_station)
        to_station_code = data.get(to_station)

        query_param = 'leftTicketDTO.train_date={}&' \
                      'leftTicketDTO.from_station={}&' \
                      'leftTicketDTO.to_station={}&' \
                      'purpose_codes=ADULT' \
            .format(train_date, from_station_code, to_station_code)

        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?'

        full_url = url + query_param
        resp = self.session.get(full_url, headers=self.headers)
        if resp.status_code == 200 and resp.url == full_url:
            print('query_ticket() 成功!然后进行车票清理工作!')
            self._get_train_info(resp.json(), from_station, to_station)

        else:
            print('query_ticket() error! status_code:{}, url:{}\norigin_url:{}'
                  .format(resp.status_code, resp.url, full_url))

    def _get_train_info(self, text, from_station, to_station):
        """
        功能:提取出查询到的列车信息
        :param text: 包含所有从起点站到终点站的车次信息
        :return: 返回所有车次信息
        """
        if not text:
            print('_query_train_info() error: text为:', text)
        # 把json文件转变成字典形式
        result = dict(text)
        # 判断有无车次的标志
        if result.get('data').get('map'):
            train_info = result.get('data').get('result')
            train_list = deque()
            for item in train_info:
                split_item = item.split('|')
                item_dict= {}
                for index, item in enumerate(split_item,0):
                    print('{}:\t{}'.format(index, item))
                if split_item[11] == 'Y': # 已经开始卖票了
                    item_dict['train_name'] = split_item[3] # 车次名
                    item_dict['depart_time'] = split_item[8] # 出发时间
                    item_dict['arrive_time'] = split_item[9] # 到站时间
                    item_dict['spend_time'] = split_item[10] # 经历时长
                    item_dict['wz'] = split_item[29] # 无座
                    item_dict['yz'] = split_item[28] # 硬座
                    item_dict['yw'] = split_item[26] # 硬卧
                    item_dict['rw'] = split_item[23] # 软卧
                    item_dict['td'] = split_item[32] # 特等座
                    item_dict['yd'] = split_item[31] # 一等座
                    item_dict['ed'] = split_item[30] # 二等座
                    item_dict['dw'] = split_item[33] # 动卧
                    train_list.append(item_dict)
                # 无法买票的车次,有可能是已卖光,也有可能是还不开卖
                elif split_item[0] == '':
                    print('_query_train_info():车次{}的票暂时不能购买!'
                          .format(split_item[3]))
                else:
                    print('_query_train_info():车次{}还未开始卖票,起售时间为:{}'
                          .format(split_item[3], split_item[1]))
            # 调用方法来打印列车结果
            self._print_train(train_list, from_station, to_station)
        else:
            print('_get_train_info() error: 从{}站到{}站有没列车!'
                  .format(from_station, to_station))

    def _print_train(self, train_info, from_station, to_station):
        """
        功能:打印查询到的车次信息
        :param train_info: 提取出来的车次信息
        :return:
        """

        if not train_info:
            print('_print_train() error: train_info是None!')
            return

        print('从{}到{}还有余票的列车有:'.format(from_station, to_station))
        for item in train_info:
            if 'G' in item['train_name']: # 高铁
                self._print_high_train_info(item)
            elif 'D' in item['train_name']: # 动车
                self._print_dong_train_info(item)
            else:
                self._print_train_info(item)

    def _print_high_train_info(self, item):
        """
        功能:打印高铁车次信息
        :param item: 所有高铁车次
        :return:
        """
        print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t'
              '经历时长:{:4s}\t特等座:{:4s}\t一等座:{:4s}\t二等座:{:4s}'
              .format(item['train_name'], item['depart_time'],item['arrive_time'],
                      item['spend_time'],item['td'], item['yd'], item['ed']))

    def _print_dong_train_info(self, item):
        """
        功能:打印动车的车票信息
        :param item: 所有动车车次
        :return:
        """
        print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t'
              '经历时长:{:4s}\t一等座:{:4s}\t二等座:{:4s}\t软卧:{:4s}\t动卧:{:4s}'
              .format(item['train_name'], item['depart_time'], item['arrive_time'],
                      item['spend_time'],item['yd'],item['ed'], item['rw'], item['dw']))
    def _print_train_info(self,item):
        """
        功能:打印普通列出的车次信息
        :param item: 所有普通车次
        :return:
        """
        print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t经历时长:{:4s}\t'
              '软卧:{:4s}\t硬卧:{:4s}\t硬座:{:4s}\t无座:{:4s}'
              .format(item['train_name'], item['depart_time'], item['arrive_time'],
                      item['spend_time'],item['rw'], item['yw'], item['yz'], item['wz']))
    def _query_prompt(self):
        """
        功能: 与用户交互,让用户输入:出发日期,起始站和终点站并判断其正确性
        :return: 返回正确的日期,起始站和终点站
        """

        time_flag, train_date = self._check_date()
        if not time_flag:
            print('_query_prompt() error:', '乘车日期不合理,请检查!!')
            return
        # 创建有序字典,方便取值
        query_data = OrderedDict()
        from_station = input('请输入起始站:')
        to_station = input('请输入终点站:')

        station_flag = True
        filename = 'name_code.json'
        with open(filename, 'r') as f:
            data = dict(json.load(f))
            stations = data.keys()
            if from_station not in stations or to_station not in stations:
                station_flag = False
                print('query_prompt() error: {}或{}不在站点列表中!!'
                      .format(from_station, to_station))
            # 获取起始站和终点站的代码
            from_station_code = data.get(from_station)
            to_station_code = data.get(to_station)
        query_data['train_date'] = train_date
        query_data[from_station] = from_station_code
        query_data[to_station] = to_station_code

        if time_flag and  station_flag:
            return query_data
        else:
            print('query_prompt() error! time_flag:{}, station_flag:{}'
                  .format(time_flag, station_flag))



    def _check_date(self):
        """
        功能:检测乘车日期的正确性
        :return: 返回时间是否为标准的形式的标志
        """

        # 获取当前时间的时间戳
        local_time = time.localtime()
        local_date = '{}-{}-{}'. \
            format(local_time.tm_year, local_time.tm_mon, local_time.tm_mday)
        curr_time_array = time.strptime(local_date, '%Y-%m-%d')
        curr_time_stamp = time.mktime(curr_time_array)
        # 获取当前时间
        curr_time = time.strftime('%Y-%m-%d', time.localtime(curr_time_stamp))

        # 计算出预售时长的时间戳
        delta_time_stamp = '2505600'
        # 算出预售票的截止日期时间戳
        dead_time_stamp = int(curr_time_stamp) + int(delta_time_stamp)
        dead_time = time.strftime('%Y-%m-%d', time.localtime(dead_time_stamp))
        print('合理的乘车日期范围是:({})~({})'.format(curr_time, dead_time))

        train_date = input('请输入乘坐日期(year-month-day):')
        # 把乘车日期转换成时间戳来比较
        # 先生成一个时间数组
        time_array = time.strptime(train_date, '%Y-%m-%d')
        # 把时间数组转化成时间戳
        train_date_stamp = time.mktime(time_array)
        # 获取标准的乘车日期
        train_date_time = time.strftime('%Y-%m-%d', time.localtime(train_date_stamp))
        # 做上面几步主要是把用户输入的时间格式转变成标准的格式
        # 如用户输入:2018-2-22,那么形成的查票URL就不是正确的
        # 只有是:    2018-02-22,组合的URL才是正确的!
        # 通过时间戳来比较时间的正确性
        if int(train_date_stamp) >= int(curr_time_stamp) and \
                int(train_date_stamp) <= dead_time_stamp:
            return True, train_date_time
        else:
            print('_check_date() error: 乘车日期:{}, 当前系统时间:{}, 预售时长为:{}'
                  .format(train_date_time, curr_time, dead_time))
            return False, None



def main():
    filename = 'station_name.txt'
    station = Station()
    station.station_name_code()
    station.save_station_code(filename)
    station.query_ticket()

if __name__ == '__main__':
    main()