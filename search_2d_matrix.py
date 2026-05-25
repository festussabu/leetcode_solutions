def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row = -1
    for i in range(len(matrix)):
        if matrix[i][0] <= target and target <= matrix[i][-1]:
            row = i
            break

    l = 0
    r = len(matrix[row]) - 1
    while l <= r:
        mid = (l + r) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            l = mid + 1
        elif matrix[row][mid] > target:
            r = mid - 1
        print(matrix[row][mid])
    return False

matrix = [[1,3]]
target = 3
print(searchMatrix(matrix, target))
