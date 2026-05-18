
def smallerNumbersThanCurrent( nums):

    res=[]
 
    for i in range(len(nums)):
        count = 0
        for j in range (len(nums)):
            if nums[j] < nums[i]:
                count += 1
        res.append(count)
    return res

nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))

        