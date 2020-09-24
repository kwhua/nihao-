num = input("请输入一串数字:\n")
bool1   = num.isdigit()
if bool1 == True:
    for x in range(len(num)):
        if num[x] != num[-x-1]:
            print(f"{num}不是回文数.")
            break

    else:
        print(f"{num}是回文数.")
else:
    print(f"{num}中含有非数字的符号.")