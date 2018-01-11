def plusone(digits):
    num=0
    mult=1
    for d in reversed(digits):
        num+=d*mult
        mult*=10
    num+=1
    ans=[]
    while num>0:
        ans.insert(0,num%10)
        num=int(num/10)
    return ans

digits=[1,2,4,4]
num=plusone(digits)
print(num)
