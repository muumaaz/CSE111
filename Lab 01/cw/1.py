#1
usr = input()
upperNum = 0
lowerNum = 0

for ch in usr:
    if 65 <= ord(ch) <= 90:
        upperNum += 1
    else:
        lowerNum += 1

newUsr = ''
if upperNum > lowerNum:
    for ch in usr:
        if 97 <= ord(ch) <= 122:
            newUsr += chr(ord(ch) - 32)
        else:
            newUsr += ch
else:
    for ch in usr:
        if 65 <= ord(ch) <= 90:
            newUsr += chr(ord(ch) + 32)
        else:
            newUsr += ch
print(newUsr)