# nums =[1,2,4,3,4,5,6,7,7,8,9,0,12]
# b=[]
# while nums:
#     a=nums.pop()
#     # print(a)
#     b.append(a)
#
# print(b)
def print_a(nums,b):
    while nums:
        a=nums.pop()
        print(a)
        b.append(a)
def print_b(b):
    print(b)
nums= [1,2,4,3,4,5,6,7,7,8,9,0,12]
b = []
print_a(nums,b)
print_b(b)


def save_message(name,age,gender,**other):
    a={}
    a['name']=name
    a['age']=age
    a['gender']=gender
    for x,value in other.items():
        a[x]=value
    return a
b=save_message("匡文华",18,"男",学历="本科",地址="江西省吉安市")
print(b)

