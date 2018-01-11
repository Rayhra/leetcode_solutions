def sqrt(x):
    low=0
    high=x
    while low<high:
        mid=(low+high)/2
        if mid*mid<x and (mid+1)*(mid+1)<x:
            low=mid-1
        elif mid*mid>x and (mid+1)*(mid+1)>x:
            high=mid+1
        elif (mid+1)*(mid+1)==x:
            return mid+1
        else:
            return mid
    return 0

x=-8
n=sqrt(x)
print(n)
