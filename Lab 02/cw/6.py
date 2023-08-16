#6
def capital(par):
    sp = ".!?"
    new = ''

    for i in range(len(par)):
        if i == 0:
            new += par[i].upper()
        elif par[i - 2] in sp and i != 1:
            new += par[i].upper()
        elif par[i - 1] == ' ' and par[i] == 'i' and par[i + 1] == ' ':
            new += par[i].upper()
        else:
            new += par[i]
    print(new)

text = "my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog's name? i love my pet very much."
capital(text)