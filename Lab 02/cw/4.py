#4
def palindrome(word):
    lst = word.split()
    old = ''
    for i in lst:
        old += i
    new = old[-1::-1]
    if new == old:
        print("Palindrome")
    else:
        print("Not a palindrome")



palindrome('nurses run')