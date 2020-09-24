import queue



q1 = queue.Queue(5)  # 创建一个先进先出的队列
q2 = queue.LifoQueue(5)  # 创建一个后进先出的队列
q3 = queue.PriorityQueue(5)  # 优先级队列


# put()  : 输入
q1.put(1)

# get()  : 获取
q1.get()

# qsize : 获取当前队列的长度,不是百分之百的准确
print(q1.qsize())

# empty  : 判断队列是否为空,返回的是布尔值
print(q1.empty())

# full  : 判断队列是否为满,返回为布尔值
print(q1.full())
