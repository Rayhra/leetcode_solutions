def searchinsertpos(nums, target):
    if target in nums:
        return binarysearch(nums,target,0,len(nums))
    else:
        i=0
        if nums[-1]<target:
                return len(nums)
        for n in nums:
            if n>target:
                return i
            i+=1


def binarysearch(nums,target,start,end):
    while start<=end:
        middle=int(start+(end-start)/2)
        if target==nums[middle]:
            return middle
        elif target>nums[middle]:
            start=middle+1
        else:
            end=middle-1


nums=[9]
target=9
val=searchinsertpos(nums,target)
print(val)
