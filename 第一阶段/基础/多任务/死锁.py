import threading
import time


def test1():
    # 锁A上锁
    if lockA.acquire():
        print("test1的锁A....")
        time.sleep(0.4)
        # 锁B上锁
        if lockB.acquire():
            print("test1的锁B....")
            # 释放锁B
            lockB.release()
            print("test1的释放锁B....")
        else:
            print("test1没有获得锁B")
        # 释放锁A
        lockA.release()
        print("test1的释放锁A....")
    else:
        print("test1没有获得锁A")


def test2():
    # 锁B上锁
    if lockB.acquire():
        print("test2的锁B....")
        # 锁A上锁
        if lockA.acquire(timeout=1):  # 等待1秒,没有获得锁A,就会自动放弃
            print("test2的锁A....")
            # 释放锁A
            lockA.release()
            print("test2的释放锁A....")
        else:
            print("test2没有获得锁A")
        # 释放锁B
        lockB.release()
        print("test2的释放锁B....")
    else:
        print("test2没有获得锁B")

# 创建锁对象
lockA = threading.Lock()
lockB = threading.Lock()

if __name__ == "__main__":
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()
