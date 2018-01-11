#Implement strStr().
#Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if not needle in haystack:
        return -1
    if not haystack and not needle:
        return 0
    x=len(needle)
    for i in range(len(haystack)-x+1):
        if needle==haystack[i:i+x]:
            return i


haystack="blahblahmundo"
needle="mundo"
val=strStr(haystack, needle)
print(val)
