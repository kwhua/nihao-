"""
项目分析
一 首页---展示信息
    1 新用户注册
    2 用户登陆
        2.1 普通用户登陆
        2.2 管理员登陆

    3 退出系统

二 用户注册
    需要提供姓名、学号、密码 ----定义学生字典保存学生信息

三 用户登陆
    1 输入用户名和密码
    2 验证
    3 登陆成功后展示用户可以操作的功能
        3.1 查看/修改个人信息
            展示个人信息
            询问是否需要修改
        3.2 课程
            3.2.1 展示全部课程
            3.2.2 根据展示情况选课
    4 退出登录，返回首页

四 管理员登陆
    1 课程管理
        增、删、改，查
    2 用户管理
        用户的增删改查
    3 退出登录，返回首页


"""
# 准备工作
# 定义字典保存学生信息
# stu_info = dict()  # {user_name:{user_info}}
stu_info = {
    'zs':{"name":"zs","password":"111111",'stu_num':1,'course':set()},
'张三':{"name":"zs","password":"111111",'stu_num':1,'course':set()}
}

# 创建管理员账户
admin = {'name':'admin','password':'admin'}

# 定义初始课程列表
course_info = ['语文','数学','英语','计算机']



# 一 首页---展示信息

while True:
    print("~~~~~~~~~**********~~~~~~~~~~")
    print('欢迎来到优就业自助选课系统')
    print('    1 用户注册')
    print('    2 用户登陆')
    print('    3 退出系统')
    print("~~~~~~~~~**********~~~~~~~~~~")

    # 用户输入
    operate_id = input('\n请输入您要执行的操作编号：')
    while operate_id != '3':
        # 用户注册
        if operate_id == '1':
            print('欢迎进入注册页面，请按照要求填写如下信息：')

            # 输入信息
            user_name = input("请输入用户名：")
            password = input('请输入密码（至少6位）：')
            stu_number = input('请输入学号：')


            # 校验用户名是否存在
            if user_name in stu_info:
                print("用户名已存在，请更换名称")
                continue

            # 校验密码
            if len(password) < 6:
                print("密码长度不够，请重新输入")
                continue

            # 将学生信息存入字典,默认所选课程为空集合
            stu_info[user_name] = {'name':user_name,'password':password,'stu_num':stu_number,'course':set()}
            print("注册成功！")
            break

        # 登陆
        elif operate_id == '2':
            print('欢迎来到登陆页面')
            input_name = input("请输入用户名：")
            input_pwd = input("请输入密码：")
            if input_name == 'admin'and input_pwd == admin['password']:
                print("欢迎管理员登陆")
                # 展示菜单
                while True:
                    print("~~~~~~~~~**********~~~~~~~~~~")
                    print('======1 课程管理=======    ')
                    print('     1.1 增加课程')
                    print('     1.2 删除课程')
                    print('     1.3 修改课程')
                    print('     1.4 查看课程')
                    print("======2 用户管理=======    ")
                    print('     2.1 增加用户')
                    print('     2.2 删除用户')
                    print('     2.3 修改用户')
                    print('     2.4 查看用户')
                    print('======3 退出登陆=======    ')
                    print("~~~~~~~~~**********~~~~~~~~~~")

                    admin_operate_id = input("请输入操作对应编号：")
                    if admin_operate_id == '1.1':
                        pass
                    elif admin_operate_id == '1.2':
                        pass
                    elif admin_operate_id == '1.3':
                        pass
                    elif admin_operate_id == '1.4':
                        pass
                    elif admin_operate_id == '2.1':
                        pass
                    elif admin_operate_id == '2.2':
                        pass
                    elif admin_operate_id == '2.3':
                        pass
                    elif admin_operate_id == '2.4':
                        pass
                    elif admin_operate_id == '3':
                        break
                    else:
                        print("输入有误，请重新输入！")

            elif input_name in stu_info:
                if not input_pwd == stu_info[input_name]['password']:
                    print("密码输入有误！请重新输入")
                    continue
                print(f"欢迎{input_name}登陆！")
                # 展示菜单
                while True:
                    print("~~~~~~~~~**********~~~~~~~~~~")
                    print('======1 个人资料=======    ')
                    print('     1.1 查看信息')
                    print('     1.2 修改信息')
                    print("======2 课程管理=======    ")
                    print('     2.1 查看课程')
                    print('     2.2 增加课程')
                    print('======3 退出登陆=======    ')
                    print("~~~~~~~~~**********~~~~~~~~~~")

                    stu_operate_id = input("请输入操作对应编号：")
                    if stu_operate_id == '1.1':
                        print("您的信息如下：")
                        print(stu_info[input_name])
                    elif stu_operate_id == '1.2':
                        change_info_id = input("请输入您要修改的信息)\n1姓名\t2密码：")
                        if change_info_id == '1':
                            new_name = input("请输入新的姓名：")
                            if new_name not in stu_info:
                                # 修改原信息
                                stu_info[input_name]['name'] = new_name  # input_name = zs
                                stu_info[new_name] = stu_info[input_name]
                                # 将旧的学生信息删除
                                stu_info.pop(input_name)   # zs  ls
                                input_name = new_name
                                print("姓名修改成功！")
                            else:
                                print("用户名重复")
                        elif change_info_id == '2':
                            new_pwd = input('请输入新密码：')
                            if len(new_pwd) >=6:
                                stu_info[input_name]['password'] = new_pwd
                                print("密码修改成功！")

                    elif stu_operate_id == '2.1':
                        print("全部课程信息如下：")
                        print(course_info)
                    elif stu_operate_id == '2.2':
                        add_course_name = input('请输入要增加的课程名称：')
                        if add_course_name in course_info:
                            stu_info[input_name]['course'].add(add_course_name)
                            print("课程增加成功")
                        else:
                            print("课程不存在")

                    elif stu_operate_id == '3':
                        break

                    else:
                        print("输入有误，请重新输入！")

            else:
                print('输入的用户不存在，请先注册！')
                break

            if not input("是否继续进行其他操作yes/no:") == 'yes':
                break

        else:
            print('输入有误，请重新输入')
            operate_id = input('\n请输入您要执行的操作编号：')

    # 退出
    if operate_id == '3':
        print("欢迎再次登陆，再见！")
        break





