new_dict={}
while True:
    num=input()
    if(num=='STOP'):
        break
    #n20=int(n10)
    if num not in new_dict:
        new_dict[num]=1
    else:
        new_dict[num]+=1
for k,v in new_dict.items():
    print(f" {k} - {v} times")