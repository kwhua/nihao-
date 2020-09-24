'''
    在前一个示例中，我们告诉用户有一个文件找不到。但并非每次捕获到异常时都需要告诉用
户，有时候你希望程序在发生异常时一声不吭，就像什么都没有发生一样继续运行。要让程序在
失败时一声不吭，可像通常那样编写try代码块，但在except代码块中明确地告诉Python什么都不
要做。Python有一个pass语句，可在代码块中使用它来让Python什么都不要做：
'''
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename)as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.strip()
        num_words = len(words)
        print(f"{filename}中一共包含了{num_words}个单词.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

'''
    相比于前一个程序，这个程序唯一不同的地方是 Ø 处 的 pass 语句。现在，出现
FileNotFoundError异常时，将执行except代码块中的代码，但什么都不会发生。这种错误发生时，
不会出现traceback，也没有任何输出。用户将看到存在的每个文件包含多少个单词，但没有任何
迹象表明有一个文件未找到：
The file alice.txt has about 29461 words. 
The file moby_dick.txt has about 215136 words. 
The file little_women.txt has about 189079 words. 
    pass语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这
里做些什么。例如，在这个程序中，我们可能决定将找不到的文件的名称写入到文件
missing_files.txt中。用户看不到这个文件，但我们可以读取这个文件，进而处理所有文件找不到
的问题。
'''