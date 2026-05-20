def two(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

 

nums = [2,7,0,15,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88]
target = 88

result = two(nums, target)

print(result)