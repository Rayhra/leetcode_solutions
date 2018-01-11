def addbinary(a,b):
    la=len(a)
    lb=len(b)
    if la<lb:
        a='0'*(lb-la)+a
    elif lb<la:
        b='0'*(la-lb)+b
    ans=""
    carry=0
    for i in range(len(a),0,-1):
        if a[i-1]=='1' and b[i-1]=='1':
            if carry==1:
                ans='1'+ans
            else:
                ans='0'+ans
                carry=1
        elif a[i-1]=='0' and b[i-1]=='0':
            if carry==1:
                ans='1'+ans
                carry=0
            else:
                ans='0'+ans
        else:
            if carry==1:
                ans='0'+ans
            else:
                ans='1'+ans
                carry=0
    if carry==1:
        ans='1'+ans
    return ans
a='1'
b='100'
ans=addbinary(a,b)
print(ans)
