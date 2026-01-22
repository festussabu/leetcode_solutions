def twoSum(nums, target):
    hash_map = {}
    if nums:
        for i, value in enumerate(nums):
            complement = target - value
            if complement in hash_map:
                return hash_map.get(complement), i
            else:
                hash_map[value] = i
        return("Element not found")



            

    

nums = [2,11,7,15]
target = 9
print(twoSum(nums, target))



# Case 1
# Input: nums = [2,11,7,15], target = 9
# Expected: [0,2]
#
# Case 2
# Input: nums = [3,3], target = 6
# Expected: [0,1]


# Time: O(n)
# Space: O(n)
