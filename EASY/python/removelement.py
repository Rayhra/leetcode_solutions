def removelement(nums,val):
    if not nums:
        return 0
    j=0
    for i in range(len(nums)):
        if nums[j]==val:
            nums.pop(j)
        else:
            j+=1
    print(nums)
    lenght=len(nums)
    return lenght
nums=[3,2,2,3]
val=3
lenght=removelement(nums,val)
print(lenght)
