import math
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = ''
    matrix = [[] for _ in range(numRows)]

    row = 0
    direction = 1

    for ch in s:
        matrix[row].append(ch)

        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1

        row += direction

    for i in matrix:
        for j in i:
            res+=str(j)
    return res


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
# Output: "PAHNAPLSIIGYIR"
# T: O(n)
# S: O(n)
# where n is the lenght of string
