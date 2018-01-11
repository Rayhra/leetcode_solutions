
def reverseint(x):
    ans=0
    flagneg=False
    if x<0:
        x=-x
        flagneg=True
    while x>0:
        ans=ans*10+x%10
        x=int(x/10)
        if ans>int32:
            return 0
    if flagneg:
        return -ans
    else:
        return ans
int32= 2147483647
x=1534236469
ans=reverseint(x)
print(ans)
