ticket = input("你是否有票:[yes/no]\n")
if ticket == 'yes':
    knife = input("行李包里是否有刀:[yes/no]\n")
    if knife == 'yes':
        print("要求交出刀具,重新检查")
    elif knife == 'no':
        print("祝您旅行愉快!")

else:
    print("请前往售票窗口购票,谢谢.")
