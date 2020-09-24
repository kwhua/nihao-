print("欢迎光临淘宝网")
while True:
    operation = input("请输入你需要的功能:[注册/登录]\n")
    list_id = ['123456']
    list_pwd = ['123']
    if operation == '注册':
        while True:
            id_ = input("注册的账号:\n")
            if id_ == '123456':
                print("该账号已被注册!")
                continue
            else:
                pwd = input("请输入账号的密码:\n")
                list_id.append(id_)
                list_pwd.append(pwd)
                print("恭喜你注册成功!")
                break
    elif operation == '登录':
        i = 3
        count = 0
        while i >= 1:
            count += 1
            if count > 0:
                input_id = input("输入你的账号:\n")
                for x in list_id:
                    if x != input_id:
                        print(f"你输入的账号或密码有误,还剩{3 - i}次机会!")
                        continue
                    i -= 1
                else:
                    num = list_id.index(input_id)
                    input_pwd = input("请输入账号的密码:\n")
                    if list_pwd[num] == input_pwd:
                        print("欢迎登录!")
                        print("是否需要更改密码:[yes/no]\n")
                        operation_ = input("是否需要更改密码:[yes/no]\n")
                        if operation_ == 'yes':
                            mark = True
                            while mark:
                                new_pwd = input("输入新密码:\n")
                                again_pwd = input("再次确认密码:\n")
                                if new_pwd == again_pwd:
                                    list_pwd[num] = new_pwd
                                    print(f"修改成功,你的新密码是:{new_pwd}")
                                    print("正在退出...")
                                    mark = False
                                else:
                                    print("两次输入密码不一致,请重新输入!")
                                    mark = True
                            else:
                                break

            else:
                print("3次机会已用尽,请您联系柜台!")
    else:
        break