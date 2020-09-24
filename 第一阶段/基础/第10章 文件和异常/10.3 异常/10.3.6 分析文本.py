'''
    你可以分析包含整本书的文本文件。很多经典文学作品都是以简单文本文件的方式提供的，
因为它们不受版权限制。本节使用的文本来自项目Gutenberg（http://gutenberg.org/），这个项目提
供了一系列不受版权限制的文学作品，如果你要在编程项目中使用文学文本，这是一个很不错的
资源。
    下面来提取童话Alice in Wonderland的文本，并尝试计算它包含多少个单词。我们将使用方
法split()，它根据一个字符串创建一个单词列表。下面是对只包含童话名"Alice in Wonderland"
的字符串调用方法split()的结果：
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
'''
'''
    方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。为计算Alice in
Wonderland包含多少个单词，我们将对整篇小说调用split()，再计算得到的列表包含多少个元
素，从而确定整篇童话大致包含多少个单词：
'''
try:
    with open('alice.txt') as f:
        contents = f.read()
except FileNotFoundError:
    print('文件未创建,请创建文件.')
else:
    words = contents.strip()
    num_words = len(words)
    print(f"这个文件{f}一共有{num_words}个单词.")
# 我们把文件alice.txt移动到正确的目录中,让try代码块能够成功地执行.








