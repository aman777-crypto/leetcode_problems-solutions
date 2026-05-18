def find(nums,target):

    
    left=0
    right = len(nums) -1
    

    while left < right :
        total = nums[left] + nums[right]
  

        if total == target:
            return [left+1,right+1]
        
        elif total < target:

            left += 1
        else:
            right -=1

nums=[1,1,1,1,2,2,2,2,3,3,3,3,7]

#[1+1,3+1] =[]
target=9
print(find(nums,target))