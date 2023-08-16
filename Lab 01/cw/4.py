#4
s1 = input()
s2 = input()
new = ''

for i in s1:
    for j in s2:
        if i == j:
            new += i
            break

for i in s2:
    for j in s1:
        if i == j:
            new += i
            break

if new == '':
    print("Nothing in common.")
print(new)