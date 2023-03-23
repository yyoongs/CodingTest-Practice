def solution(nums):
    n = len(nums) // 2
    hash_map = {}
    for num in nums:
        if hash_map.get(num):
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    return n if len(hash_map) >= n else len(hash_map)