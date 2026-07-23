
def largest(arr):
    max_count = 0
    for i in range(len(arr)):
            
            
            if arr[i] > max_count:

                max_count = arr[i]
    return max_count
        


            
arr = [1, 8, 7, 56, 90]

print(largest(arr))