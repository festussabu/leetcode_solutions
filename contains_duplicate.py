from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    # Write your solution here
    contains = set()
    for i in range(len(nums)):
        if nums[i] not in contains:
            contains.add(nums[i])
        elif nums[i] in contains:
            return True
    return False

print(containsDuplicate([1, 2, 3, 4, 5]))
            
#time / space O(n)
