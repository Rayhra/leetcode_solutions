def roman2int(var):
    total=0
    aux=roman[var[0]]
    for i in range(len(var)-1):
        if roman[var[i]]==roman[var[i+1]]:
            aux+=roman[var[i+1]]
        elif roman[var[i]]>roman[var[i+1]]:
            total+=aux
            aux=roman[var[i+1]]
        else:
            total+=roman[var[i+1]]-aux
            aux=0
    total+=aux
    return total
    
roman={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
var='MMMCMXCIX'
total=roman2int(var)
print(total)
