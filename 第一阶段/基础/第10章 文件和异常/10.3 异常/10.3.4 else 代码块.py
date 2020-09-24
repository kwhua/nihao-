'''
    通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。错
误是执行除法运算的代码行导致的，因此我们需要将它放到try-except代码块中。这个示例还包
含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：
'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quilt.")
while True:
    first_num = input("请输入除数:\n")
    # try:
    #     first_num = first_num
    # except ValueError:
    #     print("输入的除数无效.")
    if first_num == 'q':
        break
    second_num = input("请输入被除数:\n")
    # try:
    #     first_num = first_num
    # except ValueError:
    #     print("输入的除数无效.")
    try:
        trade = float(first_num) / float(second_num)
    except ValueError:
        print("输入的只能是数字!!")
    except ZeroDivisionError:
        print("被除数不能为0\n")
    else:
        print("%.2f" %trade )
'''
    try-except-else代码块的工作原理大致如下:Python尝试执行try代码块中的代码:只有可
引发异常的代码才需要仿造try语句中.有时候,有一些仅在try代码块成功执行时才可以运行
的代码;这些代码应放在else代码块中.except代码块告诉Python,如果尝试运行try代码块中
的代码时引发了指定的异常应该怎么办.
    通过预测可能发生错误的代码,可编写健壮的程序,它们即便面临无效数据或缺少资源,也
能继续运行,从而能够抵御无意的用户错误和恶意的攻击.
'''