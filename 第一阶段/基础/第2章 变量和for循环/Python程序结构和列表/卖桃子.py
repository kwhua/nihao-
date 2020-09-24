# 桃子3元一斤
peach = 3
print("桃子3元/斤.")
# 顾客购买重量
weight = float(input("你输入购买的重量:[斤]\n"))
# 总价
total = peach * weight
print(f"你需要支付{total}元.")
# 顾客身上有多少钱
money = float(input("请输入您的金额:[元]\n"))
# 判断输入金额和总价的关系
if money > total:  # 这是大于的情况
    print(f"支付成功,找您{'{:.2f}'.format(money - total)}元,欢迎再次光临!")
elif money < total:  # 这是小于的情况
    print(f"你输入的金额不够,还需支付{'{:.2f}'.format(total - money)}元.")
else:  # 等于的情况
    print("支付成功,欢迎再次光临!")
