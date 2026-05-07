from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    l = 0
    r = len(s1) 
    for i in range(len(s2)):
        if Counter(s2[l:r]) == Counter(s1):
            return True
        l+=1 
        r+=1
    return False
        


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
