'''
完成学生选课系统
		需求分析：
		管理员 事先设置好管理员账号密码
			管理员功能：
			  查看有哪些课程,Python，java，web，unity，UI
			  增加或删除课程内容，增加 软件测试课程，删除UI课程
'''
import log_in
import time
student_material = {
    'zs': {"name": 'zs', "password": '123456', 'student_id': 2020001, "age": 20, "gender": '男',
           "course": ['Python', 'web', 'UI']}}
admin = {'admin': {"name": 'admin', "password": '999999'}}


def home():
    # 首页信息
    str1 = '欢迎登录xx大学官网'
    str4 = '===== 注  册 ====='
    str2 = '===== 登  录 ====='
    str5 = '===== 退  出 ====='
    str3 = '**********'

    print(str3.center(42, "~"))
    print(str1.center(40, " "))
    print(str4.center(44, " "))
    print(str2.center(44, " "))
    print(str5.center(44, " "))
    print(str3.center(42, "~"))
    log_in.operater()

def time_(fn):
    def inner():
        time.time()
        res = fn
        return res


    return inner


@time_
def  f():
    home


