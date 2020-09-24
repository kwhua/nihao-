def f1():
    print("f1")


def f2():
    print("f2")
    f1()


f2()


def num_(num):
    sum = 0
    if num == 0:
        return
    print(num)
    sum += num
    num -= 1
    num_(num)
    print("----------------")


num_(100)

# 3
# 2
# 1
# ----------------
# ----------------
# ----------------
n = 20
a = 1
b = 1
for x in range(1, n + 1):
    if x == 1 or x == 2:
        print(1)
    else:
        print(a + b)
        a, b = b, a + b
print("-"*50)

def sum_(n):
    sum = 0
    if n == 0:
        return
    else:
        n -= 1
        sum += n
        return sum_(sum)

print(sum_(100))
