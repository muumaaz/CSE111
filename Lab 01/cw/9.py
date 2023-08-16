time=[int(num) for num in input().split()]
play=[int(k) for k in input().split()]
count=0
for i in range(len(play)):
    if 5-play[i]>=time[1]:
        count+=1
total=count//3
print(total)