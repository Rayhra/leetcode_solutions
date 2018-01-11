def ispalindrome(x):
    ans=0
    if x<0:
        return False
    elif x>=0 and x<10:
        return True
    else:
        digits=0
        aux=x
        while aux>0:
            aux=int(aux/10)
            digits+=1
        for i in range(int(digits/2)):
            ans=ans*10+x%10
            x=int(x/10)
        if digits%2!=0:
            x=int(x/10)
        if x==ans:
            return True
        else:
            return False
x=-43
ans=ispalindrome(x)
print(ans)
