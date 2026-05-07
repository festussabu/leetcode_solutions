def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    l = 0
    r = 1
    prof = 0
    while r < n:
        curr_prof = prices[r] - prices[l]
        if prices[l] < prices[r]:
            prof = max(prof, curr_prof)
        else:
            l = r
        r+=1
    return prof



prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
