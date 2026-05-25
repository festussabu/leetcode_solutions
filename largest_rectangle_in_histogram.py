def largestRectangleArea(heights: List[int]) -> int:
    st = []
    max_ = 0

    for i, h in enumerate(heights):
        start = i
        while st and st[-1][1] > h:
            idx, height = st.pop()
            max_ = max(max_, height * (i - idx))
            start = idx
        st.append((start, h))

    for idx, height in st:
        max_ = max(max_, height * (len(heights) - idx))

    return max_

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
