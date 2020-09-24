import threading

stus = threading.local()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def process_stu(name, age):
    stu = Student(name, age)
    stus.stu = stu
    do_task1()
    do_task2()


def do_subtask1():
    stus.stu.name = 'new_' + stus.stu.name
    print(f"修改后姓名：{stus.stu.name}")


def do_subtask2():
    stus.stu.age = 5 + stus.stu.age
    print(f"修改后年龄{stus.stu.age}")


def do_task1():
    print(stus.stu.name)
    do_subtask1()


def do_task2():
    print(stus.stu.age)
    do_subtask2()


if __name__ == '__main__':
    threading.Thread(target=process_stu, args=('zs', 20)).start()
    threading.Thread(target=process_stu, args=('ls', 40)).start()
