class Solution:
    def thirdMax(nums):

        nums = list(set(nums))

        nums.sort(reverse = True)
        

        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]
    n=[1,2]
    print(thirdMax(n))

    

        