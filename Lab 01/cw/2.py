#2
def char_check(usr):
    num_bool, chr_bool = False, False

    for i in usr:
        if i in "0123456789":
            num_bool = True
        else:
            chr_bool = True

    if num_bool == True and chr_bool == True:
        print("MIXED")
    elif num_bool == True:
        print("NUMBER")
    elif chr_bool == True:
        print("WORD")

usr = input()
char_check(usr)