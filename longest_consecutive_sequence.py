def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    for i in num_set:
        if i - 1 not in num_set:
            curr = i
            streak = 1
            while curr + 1 in num_set:
                curr += 1
                streak += 1
            longest = max(longest, streak)
        continue
    return longest


nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100,4,200,1,3,2]
nums = [1,0,1,2]
print(longestConsecutive(nums))

#T=O(n)
#S=O(n)
