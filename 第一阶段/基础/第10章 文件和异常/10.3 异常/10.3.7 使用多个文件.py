


'''
    下面多分析几本书.这样做之前,我们先将这个程序大部分代码移到一个名为
count_words()的函数中,这样对多本书进行分析将更容易:
'''
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename)as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename}文件未创建,请先创建.")
    else:
        words = contents.strip()
        num_words = len(words)
        print(f"{filename}中一共包含了{num_words}个单词.")

filename = 'alice.txt'
count_words(filename)
'''
    这些代码大都与原来一样，我们只是将它们移到了函数count_words()中，并增加了缩进量。
修改程序的同时更新注释是个不错的习惯，因此我们将注释改成了文档字符串，并稍微调整了一
下措辞。
    现在可以编写一个简单的循环，计算要分析的任何文本包含多少个单词了。为此，我们将要
分析的文件的名称存储在一个列表中，然后对列表中的每个文件都调用count_words()。我们将
尝试计算Alice in Wonderland、Siddhartha、Moby Dick和Little Women分别包含多少个单词，它们
都不受版权限制。我故意没有将siddhartha.txt放到word_count.py所在的目录中，让你能够看到这
个程序在文件不存在时处理得有多出色：
'''
def count_words(filename):
    '--snip--'
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
# 文件siddheartha.txt不存在,但十号不影响这个程序处理其他文件:
'''
The file alice.txt has about 29461 words. 
Sorry, the file siddhartha.txt does not exist. 
The file moby_dick.txt has about 215136 words. 
The file little_women.txt has about 189079 words.

    在这个示例中，使用try-except代码块提供了两个重要的优点：避免让用户看到traceback；
让程序能够继续分析能够找到的其他文件。如果不捕获因找不到siddhartha.txt而引发的
FileNotFoundError异常，用户将看到完整的traceback，而程序将在尝试分析Siddhartha后停止运
行——根本不分析Moby Dick和Little Women。
'''
