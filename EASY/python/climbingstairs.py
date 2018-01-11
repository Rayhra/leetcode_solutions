def climbing_stairs(n):
    if n==1:
        return 1

    x=[0]*n
    x[0]=1
    x[1]=2
    for i in range(2,n):
        x[i]=x[i-1]+x[i-2]
    #print(x)
    return x[n-1]
n=5
ways=climbing_stairs(n)
print(ways)
