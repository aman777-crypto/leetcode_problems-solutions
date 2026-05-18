def freq(nums):

    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        return count 

   


nums=[1,1,1,1,1,1,2,3]
a= freq(nums)
print(a)