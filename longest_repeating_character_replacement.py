def characterReplacement(s: str, k: int) -> int:
    l = 0
    longest = 0
    freq= [0] * 26
    for r in range(len(s)):
        freq[ord(s[r]) - 65] +=1 
        while (r-l + 1) - max(freq) > k:
            freq[ord(s[l]) - 65] -= 1
            l+=1 
        print(longest)
        longest = max((r-l + 1), longest)
    return longest


s = "ABAB"
s = "ABBB"
s = "AABABBA"
s = "ABCDE"
k = 1
print(characterReplacement(s, k))

