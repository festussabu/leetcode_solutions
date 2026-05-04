def maxArea(height: List[int]) -> int:
    n = len(height)
    left, right = 0, n - 1
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(area, max_area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
        
    return max_area    

height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
height =[8,7,2,1]
print(maxArea(height))

#T = O(n)
#S = O(1)
