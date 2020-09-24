'''

'''
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f'{y} x {x} = {x * y}', end="\t")
    print()

# x = int(input("请输入一个数字:\n"))
# for i in range(1, x + 1):
#     print((x+1 - i) * " ", end="")
#     for j in range(1, 2*i ):
#         print("*", end="")
#     print()

# n=eval(input("输入打印的行数：\n"))
# for i in range(1,n+1):
#     a=(n-i)*' '
#     print(a,end='\t')
#     for j in range(1,i+1):
#         print(i-j+1,end='\t')
#         if (i-j+1)==1:
#             if i!=1:
#                 for k in range(2,i+1):
#                     print(k,end='\t')
#     print()

for x in range(2, 101):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        print(x)

