# form  mian import student_material,admin


def operater():
    # 用户输入功能
    while True:
        operate = input("请输入你需要的功能[注册/登录/退出]:\n")
        if operate == '注册':
            login()
        elif operate == '登录':
            log_in()
        elif operate == '退出':
            print("正在退出....")
            break
        else:
            print("输入有误,重新输入.")


def login():
    # 学生注册信息
    mark = True
    while mark:
        user_name = input("请输入用户名[只能由字母和数字组成]:\n")
        bool3 = user_name.isalnum()
        if bool3 == True:
            if user_name in student_material:
                print(f"{user_name}已注册,请重新输入.")
                continue
            else:
                while mark:
                    print("输入退出,退出注册.")
                    student_id = input("请输入你的学号:\n")
                    if student_id != '退出':
                        bool2 = student_id.isdigit()
                        if bool2 != True:
                            print("输入的学号有误,请重新输入!")
                            continue

                        else:
                            bool1 = student_id.startswith('2020')
                            if bool1 != True:
                                print("学号是以2020开头的纯数字,请重新输入")
                            else:
                                for x in student_material:
                                    for y in student_material[x]:
                                        if y == 'student_id':
                                            if student_material[x][y] == int(student_id):
                                                print(f"该{student_id}已被注册!")
                                                print("如果无误,请联系导员.")

                                else:
                                    while mark:
                                        password = input("请输入密码[最少6位数]:\n")
                                        if len(password) < 6:
                                            print("密码最少6位.")
                                            continue
                                        again_password = input("请再次确认密码:\n")
                                        if password != again_password:
                                            print("两次输入的密码不一致.")
                                            continue
                                        else:
                                            student_material[user_name] = {'name': user_name,
                                                                           "password": password,
                                                                           "student_id": student_id,
                                                                           "course": []}
                                            print(f"恭喜{user_name}注册成功!")
                                            print("正在回到首页....")
                                            mark = False
                    else:
                        break
        else:
            print("你输入的用户名不合法.")


def log_in():
    # 登录系统
    while True:
        user_name = input("请输入用户名:\n")
        if user_name in student_material:
            password = input("请输入密码:\n")
            if student_material[user_name]["password"] == password:
                print(f"{user_name},欢迎登录!")
                # 展示菜单
                while True:
                    print("~~~~~~~~~**********~~~~~~~~~~")
                    print('======1 个人资料=======    ')
                    print()
                    print('======2 退出登陆=======    ')
                    print("~~~~~~~~~**********~~~~~~~~~~")
                    operate = input("请输入对应操作的编号:\n")
                    if operate == "1":
                        print('     1.1 查看信息')
                        print('    1.2 修改信息')
                        operate1 = input("请输入对应操作的编号:\n")
                        if operate1 == "1.1":
                            print("你的信息如下:")
                            print(student_material[user_name])
                        elif operate1 == "1.2":
                            operate2 = input("请输入你需要修改的信息:[用户名\密码]\n")
                            print("输入退出,返回上一层.")
                            if operate2 == '用户名':
                                new_name = input("请输入用户名[只能由字母和数字组成]:\n")
                                bool1 = new_name.isalnum()
                                if bool1 == True:
                                    if new_name not in student_material:
                                        # 修改信息
                                        student_material[new_name]["name"] = new_name
                                        student_material[user_name] = student_material[new_name]
                                        # 将原来的信息删掉
                                        student_material.pop(user_name)
                                        new_name = user_name
                                        print(f"用户名{new_name}修改成功")
                                    else:
                                        print("输入的用户名重复.")
                                else:
                                    print("输入的用户名不合法!")
                            elif operate2 == '密码':
                                new_password = input("请输入新密码:\n")
                                if len(new_password) < 6:
                                    print("密码最少6位.")
                                student_material[user_name]['password'] = new_password
                            else:
                                print("只能修改用户名和密码.")
                                break
                        elif operate1 == '退出':
                            continue
                        else:
                            print("请输入有误,请重新输入!")
                    elif operate == "2":
                        print("正在退出登录...")
                        break
                    else:
                        print("请输入有误,请重新输入!")
            else:
                print("输入的密码有误.")
        elif user_name in admin:
            password = input("请输入密码:\n")
            if admin[user_name]["password"] == password:
                print(f"{user_name},欢迎登录!")
                # 展示菜单
                while True:
                    print("~~~~~~~~~**********~~~~~~~~~~")
                    print('======1 个人资料=======    ')
                    print()
                    print("======2 课程管理=======    ")
                    print()
                    print('======3 退出登陆=======    ')
                    print("~~~~~~~~~**********~~~~~~~~~~")
                    operate = input("请输入对应操作的编号:\n")
                    if operate == "1":
                        print('     1.1 查看信息')
                        print('     1.2 修改信息')
                        operate1 = input("请输入对应操作的编号:\n")
                        if operate1 == "1.1":
                            print("你的信息如下:")
                            print(admin[user_name])
                        elif operate1 == "1.2":
                            operate2 = input("请输入你需要修改的信息:[用户名\密码]\n")
                            print("输入退出,返回上一层.")
                            if operate2 == '用户名':
                                new_name = input("请输入用户名[只能由字母和数字组成]:\n")
                                bool1 = new_name.isalnum()
                                if bool1 == True:
                                    if new_name not in admin:
                                        # 修改信息
                                        admin[new_name]["name"] = new_name
                                        admin[user_name] = admin[new_name]
                                        # 将原来的信息删掉
                                        admin.pop(user_name)
                                        new_name = user_name
                                        print(f"用户名{new_name}修改成功")
                                    else:
                                        print("输入的用户名重复.")
                                else:
                                    print("输入的用户名不合法!")
                            elif operate2 == '密码':
                                new_password = input("请输入新密码:\n")
                                if len(new_password) < 6:
                                    print("密码最少6位.")
                                admin[user_name]['password'] = new_password
                            else:
                                print("只能修改用户名和密码.")
                                break
                        elif operate1 == '退出':
                            continue
                        else:
                            print("请输入有误,请重新输入!")
                    elif operate == '2':
                        print('     1.1 增加课程')
                        print('     1.2 删除课程')
                    else:
                        print("输入有误,重新输入.")
            else:
                print("密码输入有误,重新输入.")
        else:
            print("用户名不正确!重新输入.")
