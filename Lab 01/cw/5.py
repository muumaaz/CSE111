#5
usr = input()
low = 0
up = 0
digit = 0
sp = 0
log = ''
for i in usr:
    if 97 <= ord(i) <= 122:
        low += 1
    if 65 <= ord(i) <= 90:
        up += 1
    if i in "0123456789":
        digit += 1
    if i in " $#@":
        sp += 1

if low > 0 and up > 0 and digit > 0 and sp > 0:
    log +="OK"
if low == 0:
    log += "Lowercase Missing"
if up == 0:
    log += "Uppercase Missing"
if digit == 0:
    log += "Digit Missing"
if sp == 0:
    log += "Special Character Missing"
print(log)