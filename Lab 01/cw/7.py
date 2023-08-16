num=int(input())
adict={}
for p in range(num):
    
    list1=[int(q) for q in input().split()]
    
    adict[sum(list1)]=list1
    
list2=[k for k in adict.keys()]

print(max(list2))

print(adict[max(list2)])