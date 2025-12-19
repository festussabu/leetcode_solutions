def lengthOfLongestSubstring(s):

    t_set = set()
    L = 0
    R = 0
    best = 0

    while R < len(s):
        if s[R] not in t_set:
            t_set.add(s[R])
            best = max(best, (R - L) + 1)
            R += 1
        else:
            t_set.remove(s[L])
            L += 1
    return best


print(lengthOfLongestSubstring("pwwkew"))  # output = 3 | max(length(#bca #cab #abc))


# T: O(n)
# S: O(n)
# Approch: Sliding window with a set
