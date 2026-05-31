#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order. explain me this code 


def intersection(nums1, nums2):

    set1 = set(nums1)
    result = []

    for num in set(nums2):
        if num in set1:
            result.append(num)

    return result