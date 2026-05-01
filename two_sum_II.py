def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
           right -=1
    return []

numbers = [-1,0]
numbers = [5,25,75]
numbers = [2,7,11,15]
numbers = [0, 0, 3 ,5]
target =100
target =9
target =0
print(twoSum(numbers, target))
