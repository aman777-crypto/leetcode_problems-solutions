def duplicate(nums):
        i = 0
        for j in range(i+1,len(nums)):
            if nums[i] != nums[j]:
                return True
            i += 1
            
            return False
nums=[1,2,3]
print(duplicate(nums))