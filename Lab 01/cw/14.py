keys={'1':['.',',','?','!',':'],'2':['A','B','C'],'3':['D','E','F'],'4':['G','H','I'],'5':['J','K','L'],'6':['M','N','O'],
'7':['P','Q','R','S'],'8':['T','U','V'],'9':['W','X','Y','Z'],'0':[' ']}
text=input('').upper()
for i in text:
    for k,v in keys.items():
        if i in v:
                print(k*(v.index(i)+1),end='')