def generator():
    count = 1  # 计数

    avg = 0  # 计算平局值
    total = 0  # 用于记录和
    while True:
        get_num = yield avg
        total += get_num
        avg = total/count
        count += 1

gen = generator()

gen.send(None)
print(gen.send(200))
print(gen.send(231))
print(gen.send(12))



def generator():
    print("这是一个生成器")
    yield

gen = generator()
print(gen)  # <generator object generator at 0x000000000215C948>

gen.__next__()  # 这是一个生成器