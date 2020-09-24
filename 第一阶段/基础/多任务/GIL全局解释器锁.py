# 多进程
import queue
import threading
from multiprocessing import Process
import time


def func1():
    s_time = time.time()
    i = 0
    for _ in range(200000000):
        i += 1
    e_time = time.time()
    print(f"耗费：{e_time - s_time}")
    print(i)


def func2():
    s_time = time.time()
    i = 0
    for _ in range(6250000):
        i += 1
    e_time = time.time()
    print(f"耗费时间：{e_time - s_time}")
    print(i)


if __name__ == '__main__':
    # func1()  # 耗费：14.955855369567871
    for _ in range(32):
        Process(target=func2).start()  # 耗费时间：10.602606296539307

# 火车站的抢票系统



def buy(q, name):
    while True:
        num = q.get()
        print(f'{name}成功抢到第{num}张票')
        time.sleep(0.3)
        q.task_done()


def sale(q):
    for i in range(1, 101):
        print(f'即将开始售卖第{i}张票')
        time.sleep(0.5)
        q.put(i)


if __name__ == '__main__':
    q = queue.Queue()
    f = open('p-c.txt', 'w', encoding='utf8')
    c1 = threading.Thread(target=buy, args=(q, "zs"), daemon=True)
    c2 = threading.Thread(target=buy, args=(q, "ls"), daemon=True)
    c3 = threading.Thread(target=buy, args=(q, "ww"), daemon=True)

    p = threading.Thread(target=sale, args=(q,))

    c1.start()
    c2.start()
    c3.start()
    p.start()

    q.join()  # 注意要先结束后关闭文件
    f.close()
