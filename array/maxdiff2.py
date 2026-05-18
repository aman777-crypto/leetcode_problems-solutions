def maximumDifference(nums):
    min_num= nums[0]
    maxdiff = -1

    for num in nums[1:]:
        if min_num < num:
            maxdiff = max(maxdiff,num - min_num)
        else:
            min_num = num
    return maxdiff

                
nums = [7,1,5,4]
print(maximumDifference(nums))
