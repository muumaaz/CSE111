adict={}
bdict={}
num=input().split()
for i in range(0,len(num),2):
    adict.update({num[i]:num[i+1]})
print(adict)
for k,v in adict.items():
    if v not in bdict:
        bdict.update({v:[k]})
    else:
        bdict[v].append(k)
print(bdict)