
'''
    前面我们分析的都是一个只有三行的文本文件，但这些代码示例也可处理大得多的文件。
如果我们有一个文本文件，其中包含精确到小数点后1 000 000位而不是30位的圆周率值，也可
创建一个包含所有这些数字的字符串。为此，我们无需对前面的程序做任何修改，只需将这个
文件传递给它即可。在这里，我们只打印到小数点后50位，以免终端为显示全部1 000 000位而
不断地翻滚：
'''

with open('pi_miller.txt',encoding="utf-8") as f:
    lines = f.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    print(line)
# 注意 要运行这个程序（以及后面的众多示例）