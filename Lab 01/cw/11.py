def dict_conv(text):
    dict1={}
    for i in range(len(text)):
        k,v=text[i].split(":")
        dict1.update({k:int(v)})
    return dict1
text=input().split(",")
dic1=dict_conv(text)
text=input().split(",")
dic2=dict_conv(text)
tup=()
lst=[]
dic3=dict(dic1)
dic3.update(dic2)

for k,v in dic1.items():
    for k1,v1 in dic2.items():
        if k==k1:
            dic3[k]=int(v)+int(v1)

for v in dic3.values():
    if v not in lst:
        lst.append(int(v))
        lst.sort()
        tup=tuple(lst)
print(dic3)
print('values:',tup)