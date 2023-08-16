while True:
    num=input().split()
    if 'STOP' in num:
        break
    else:
        for p in range(len(num)):
            num[p]=int(num[p])
        lst2=[]
        s1=''
        for i in range(len(num)-1):
            lst2.append(num[i]-num[i+1])
            lst2[i]=abs(lst2[i])
        for j in range(1,len(num)):
            if j in lst2:
                s1='UB Jumper'
            
            else:
                s1="Not UB Jumper"
                break
        print(s1)