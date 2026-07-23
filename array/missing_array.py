def missing(arr):

            
    arr.sort()
        
    n = len(arr) + 1
    expect = n*(n+1) // 2
        
    actual= sum(arr)
    return (expect - actual)

n = [1,2,3,5]

print(missing(n))
        




