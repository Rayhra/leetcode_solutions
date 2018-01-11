def countandsay(n):
    if n==1:
        return "1"
    if n==2:
        return "11"
    else:
        n2="11"
        for i in range(n-2):
            c=1
            n3=""
            for j in range(len(n2)-1):
                if n2[j]==n2[j+1]:
                    c+=1
                else:
                    n3+=str(c)+n2[j]
                    c=1
            n3+=str(c)+n2[-1]
            n2=n3
        return(n2)

n=5
val=countandsay(n)
print(val)
