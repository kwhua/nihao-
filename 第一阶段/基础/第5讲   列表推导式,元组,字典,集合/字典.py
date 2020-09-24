# 练习:水果店有水果:苹果,香蕉,梨,每个水果有各自的名称,价格,数量,请展示出来
fruit_shop = {
    'apple': {"name": 'apple', "price": 4, "amount": 60},
    'banana': {"name": 'banana', "price": 3, "amount": 100},
    'pear': {"name": 'pear', "price": 3, "amount": 50}
}
for key in fruit_shop:
    print(key)
for key, value in fruit_shop.items():
    print(f"名称为:{key}的信息为:{value}")
print(type(key))
print(type(value))

zs = {'name': 'zs', 'age': 20, 'height': 170}
print(zs.popitem())
print(zs)

zs.clear()
print(zs)
