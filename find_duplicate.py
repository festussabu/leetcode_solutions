def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    new_slow = 0
    while new_slow != fast:
        new_slow = nums[new_slow]
        fast = nums[fast]
    return fast


nums = [3,1,4,2, 2]
print(findDuplicate(nums))
