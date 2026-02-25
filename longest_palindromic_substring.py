s = "gddl" # dd
s1 = "abababa" # abababa
s2 = "abcbd" # bcb
s3 = "racecar" # racecar


def longestPalindrome(s):
    longest = 0
    start = 0
    end = 0
    for i in range(len(s)):
        #odd
        left = i
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1 
            right +=1
            length = right-left - 1
            if length > longest:
                longest = length
                start = left + 1
                end = right - 1
        #even
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            length = right - left - 1
            if length > longest:
                longest = length
                start = left + 1
                end = right - 1
    return s[start:end + 1]

print(longestPalindrome(s))


#Time O(n^2)
#Space O(1)
