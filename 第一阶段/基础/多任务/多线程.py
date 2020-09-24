import time
from threading import Thread
import threading


def beat(name):
    print(f"今天由{name}揍吴族豪")

    print(f"{name}的第一拳")
    time.sleep(0.5)
    print(f"{name}的第二拳")
    time.sleep(0.5)
    print(f"{name}的第三拳")
    time.sleep(0.5)
    print(f"{name}的第四拳")
    time.sleep(0.5)
    print(f"{name}的第五拳")
    time.sleep(0.5)
    print(f"{name}揍累了,明天再揍!")
    print(f"在beat中线程：{threading.current_thread().getName()}")


def conduct(name, **kwargs):
    time.sleep(0.00001)
    print(f"{name}挨了我一拳,哭了")
    time.sleep(0.5)
    print(f"{name}愤怒了")
    time.sleep(0.5)
    print(f"{name}有点坚持不住了")
    time.sleep(0.5)
    print(f"{name}开始跪地求饶")
    time.sleep(0.5)
    print(f"{name}卒,享年{kwargs}")
    print(f"在conduct中线程：{threading.current_thread().getName()}")


if __name__ == '__main__':
    t1 = Thread(target=beat, name="beat", args=("匡文华",))
    t2 = Thread(target=conduct, name="conduct", args=("吴族豪",), kwargs={"25": "岁"})

    t1.start()
    t2.start()

    # 查看线程数量和当前线程
    print(f"第一次查看线程数量：{threading.active_count()}")
    print(f"第一次线程有：{threading.enumerate()}")
    t1.join()
    # 查看线程数量和当前线程
    print(f"第二次查看线程数量：{threading.active_count()}")
    print(f"第二次线程有：{threading.enumerate()}")
