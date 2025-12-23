import math


def findMedianSortedArrays(nums1, nums2):
    combined = nums1 + nums2
    combined.sort()
    n = len(combined)

    if n % 2 == 0:
        first_ = (n - 1) // 2
        second_ = n // 2
        median = (combined[first_] + combined[second_]) / 2.0
        return median

    middle = (n - 1) // 2
    return combined[middle]


nums1 = [1, 2]
nums2 = [3, 4]
# output = 2.00000 - [1,2,3] - O(log(m+n))
print(findMedianSortedArrays(nums1, nums2))

# S: O(m + n)
# T: O(O((m + n) log(m + n)))
# Approch: Brute Force
