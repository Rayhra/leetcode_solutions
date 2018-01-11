def longestcommonprefix(strs):
    lpc=''
    flag=True
    if not strs:
        return lpc
    s=min(strs,key=len)
    idx=strs.index(s)
    for i in range(len(strs[idx])):
        letter=strs[0][i]
        for j in range(1,len(strs)):
            if letter != strs[j][i]:
                flag=False
                break
        if flag:
            lpc+=letter
        else:
            break
    return lpc

strs=['dogin','dogtor','dogron','doginator']
lpc=longestcommonprefix(strs)
print(lpc)
