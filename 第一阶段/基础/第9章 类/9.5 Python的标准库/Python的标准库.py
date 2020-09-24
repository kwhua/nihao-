''
'''
Python标准库是一组模块,安装的Python都包含它.。可使用标准库中的任何函数和类，为此只需在程序开
头包含一条简单的import语句。
'''
# 就是将有序字典调用
'''
from collections import OrderedDict 
# 将collections里的OrderedDict类调用

favorite_languages = OrderedDict() 
# 我们创建了OrderedDict类的一个实例，并将其存储到favorite_languages中。请注意，这里没有
# 使用花括号，而是调用OrderedDict()来创建一个空的有序字典，并将其存储在favorite_languages中 。
 
favorite_languages['jen'] = 'python' 
favorite_languages['sarah'] = 'c' 
favorite_languages['edward'] = 'ruby' 
favorite_languages['phil'] = 'python' 

# 遍历favorite_languages字典,将name和language分开出来
for name, language in favorite_languages.items(): 
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")
'''