from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] +=1 
        key = tuple(count)
        anagram[key].append(s)
    return list(anagram.values())

strs = [""]
strs = ["eat","tea","tan","ate","nat","bat"] # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs))
