
#448. Find All Numbers Disappeared in an Array

#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


#Example 1:

#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]
#Example 2:
#Input: nums = [1,1]
#Output: [2]

def disappear (nums):
    res = []
    s= set(nums)

    for i in range(1,len(nums)+1):
        if i not in s:
            res.append(i)
    return res






nums=[1,1,3,5,6,7]
print(disappear(nums))

