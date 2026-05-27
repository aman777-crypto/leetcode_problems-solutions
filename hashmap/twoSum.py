def twoSum(nums,target):

    hashmap= {}

    for i, num in enumerate(nums):

        diff = target - num

        if diff in hashmap:
            return [hashmap[diff],i]
        
        hashmap[num] = i

n = [2,7,11,15]

target = 9

res = twoSum(n,target)
print(res)