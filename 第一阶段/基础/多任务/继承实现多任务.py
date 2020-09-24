import threading

import threading

import threading

# 定义全局变量
g_num = 0


def add_num1():
    """修改全局变量"""
    global g_num
    for _ in range(1000000):
        g_num += 1


def add_num2():
    """修改g_num值"""
    global g_num
    for _ in range(1000000):
        g_num += 1


if __name__ == "__main__":
    t1 = threading.Thread(target=add_num1)
    t2 = threading.Thread(target=add_num2)
    t1.start()
    t2.start()
    # 保证子线程执行结束
    t1.join()
    t2.join()
    print(f"g_num的值为{g_num}")  # 发现每次值均不同，且比2000000小
