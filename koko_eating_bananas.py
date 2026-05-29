import math
def minEatingSpeed(piles: List[int], h: int) -> int:
    if len(piles) == h:
        return max(piles)

    def find_k(k):
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
        return hours <= h
           
    l = 1
    r = max(piles)
    while l < r:
        k = (l + r)//2
        if find_k(k):
            r = k
        else:
            l = k + 1
    return r

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))
