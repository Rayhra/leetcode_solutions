def lastwordlenght(s):
    if not s:
        return
    c=0
    for i in range(len(s),0,-1):
        if s[i-1]==' ':
            return c
        c+=1
    return c



s="a"
val=lastwordlenght(s)
print(val)
