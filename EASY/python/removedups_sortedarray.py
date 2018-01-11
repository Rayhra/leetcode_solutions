def removedupsortedarray(nums):
    if not nums:
        return 0
    lenght=1
    j=1
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]:
            lenght+=1
            nums[j]=nums[i+1]
            j+=1
    print(nums)
    return lenght

nums=[1,1,2]
lenght=removedupsortedarray(nums)
print(lenght)
