flag = True
lst = []
# adding STOP
while flag:
    usr = input()
    if usr == "STOP":
        break
    else:
        lst.append(int(usr))

# List of Unique item
ref = []
for i in lst:
    if i not in ref:
        ref.append(i)


for i in ref:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    print(f"{i} - {count} times")