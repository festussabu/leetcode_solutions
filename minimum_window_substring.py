from collections import Counter

def minWindow(s: str, t: str) -> str:
    freq = Counter(t)
    required = len(freq)
    formed = 0
    best = None
    l = 0

    for r in range(len(s)):
        freq[s[r]] -= 1
        if freq[s[r]] == 0:
            formed += 1
        while formed == required:
            window = s[l:r+1]
            if best is None or len(window) < len(best):
                best = window
            freq[s[l]] += 1
            if freq[s[l]] > 0:
                formed -= 1
            l+= 1
    return best if best else ""

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
