
def maximumDifference(nums):

        maxdiff = -1

        for i in range(len(nums)):
               for j in range(1,len(nums)):


                if (nums[i]< nums[j]):
                     diff = nums[j] - nums[i]
                     maxdiff = max(maxdiff,diff)
        return maxdiff
                  
     
                
nums = [7,1,5,4]
print(maximumDifference(nums))




                    