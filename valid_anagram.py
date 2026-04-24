def isAnagram( s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_map_1 = {}
    hash_map_2 = {}
    j = 0
    for i in s:
        if i not in hash_map_1:
            hash_map_1[i] = j
        elif i in hash_map_1:
            hash_map_1[i] +=  1
    print(hash_map_1)
    for i in t:
        if i not in hash_map_2:
            hash_map_2[i] = j
        elif i in hash_map_2:
            hash_map_2[i] +=  1
    print(hash_map_2)

    if hash_map_1 == hash_map_2:
        return True
    return False
        
       

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
