def intobin(x):
    rem=x
    res=''
    while x>1:
        aux=x%2
        x=x/2
        res=res+str(aux)
    res=res+str(x)
    return res[::-1]

def hammingdist(x,y):
    dist=0
    x=intobin(x)
    y=intobin(y)
    diff=abs(len(x)-len(y))
    if len(x)>len(y):
        y=diff*'0'+y
    elif len(y)>len(x):
        x=diff*'0'+x
    for l in range(len(x)):
        if x[l]!=y[l]:
            dist+=1
    return dist

x=1
y=4
dist=hammingdist(x,y)
print(dist)
