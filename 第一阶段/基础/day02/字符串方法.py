'''
字符串方法(字符串是不可变类型)
    查找字符串的索引
        index:从左向右,只能查到第一个元素的索引
        rindex:从右向左查到的第一个元素的索引
        s ='hello world'
        s1=s.index('o')
        s2 =s.rindex('o')
        print(s1)
        print(s2)

        s = 'hello world'
        x = len(s)
        s1 = [i for i, x in enumerate(s) if x == 'l']
        print(s1)
        # 如果直接用X.index(1),只能得到0这一个索引,而我们需要所有索引.
        X = [1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 4]
        l = len(X)
        # zip_list = zip(*(range(l),X))
        # id1 = [z[0] for i,z in enumerate(zip_list) if z[1]==1]
        # 或者更简单的
        id1 = [i for i, x in enumerate(X) if x == 1]
        print(id1)

    字符串的切分 split  使用maxsplit限制切割的次数,限制次数多余时,全部切分不会报错
        split:根据指定的内容进行切分,返回一个列表,指定的元素不保留
        s ='hello world'
        s1= s.split('l',maxsplit=1)
        print(s1)

    字符串的替换 replace  __count= 代表着替换的次数
        replace:可以将指定的字符串替换成新字符串
        s ='hello world'
        s1 =s.replace('o','嗯',__count=1)
        print(s1)

    strip:去掉字符串两边指定的元素,默认去掉空格
        s ='*hello world*'
        s1=s.strip("*")
        print(s1)

    count:返回指定元素的个数
        s ='hello world'
        s1=s.count("l")
        print(s1)

    format:格式化字符串


'''
s =f'hello world{123}'
print(s)
s1 = "姓名:%s 性别:%s 年龄:%d 身高:%0.2fm"%("匡文华","男",25,1.70)
print(s1)

for x in range(1,11):
    s='http://pic.netbian.com/4kdongman/'
    s1='http://pic.netbian.com/4kdongman/{}'
    if x==1:
        print('http://pic.netbian.com/4kdongman/')
    else:
        print('http://pic.netbian.com/4kdongman/index_{}.html'.format(x))
