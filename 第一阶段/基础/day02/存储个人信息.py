def save_message(name,age,gender,**other):
    a={}
    a['name']=name
    a['age']=age
    a['gender']=gender
    for x,value in other.items():
        a[x]=value
    return a