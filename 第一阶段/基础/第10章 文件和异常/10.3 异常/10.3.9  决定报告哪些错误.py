'''
    在什么情况下该向用户报告错误呢?在什么情况下又该在失败时一声不吭呢?如果用户知道
要分析哪些文件,他们希望在有文件没有文件等稀释出现一条消息,将其中的原因告诉他们.
如果客户只想看到结果,而不是要分析哪些文件,可能就需要在哪些文件不存在时告知他们.
向用户显示他不想看待的信息可能会降低程序的可用性.Python的错误处理结构让你能够细致地
控制与用户分享错误信息的程度,要分享多少信息由你决定.
    编写得很好且经过详尽测试的代码不容易出现内部错误,入语法或逻辑错误,但只要程序依赖
于外部因素,如用户输入、存在指定的文件、有网络链接，就有可能出现异常。凭借经验可判断
该在程序的什么地方包含异常处理块，以及错误是该向用户提供多少相关的信息。
'''