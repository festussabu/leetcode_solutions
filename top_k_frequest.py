def topKFrequent(nums: List[int], k: int) -> List[int]:

    top_elements = []
    hash_map = {}
    for i in nums:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] +=1
    sorted_keys = sorted(hash_map, key=hash_map.get,reverse=True)
    for x in sorted_keys[:k]:
        top_elements.append(x)
    return top_elements


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
