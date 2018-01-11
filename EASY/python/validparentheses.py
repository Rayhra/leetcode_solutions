def validparentheses(s):
    stack=[]
    aux=''
    for p in s:
        if p=='(' or p=='{' or p=='[':
            stack.append(p)
        else:
            if not stack:
                return False
            if p==')':
                if stack.pop()!='(':
                    return False
            elif p=='}':
                if stack.pop()!='{':
                    return False
            elif p==']':
                if stack.pop()!='[':
                    return False
    if not stack:
        return True
    else:
        return False
s='[{()}]'
ans=validparentheses(s)
print(ans)
