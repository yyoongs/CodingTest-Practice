# [BOJ] 5883
# LEVEL : S4

import sys

n = int(sys.stdin.readline().rstrip())

data = []
hm = {}
for i in range(n):
    nums = int(sys.stdin.readline().rstrip())
    data.append(nums)
    if not hm.get(nums):
        hm[nums] = 1

answer = 0

for key,values in hm.items():
    temp = [ i for i in data if i not in [key]]
    max_count = 1
    prev = temp[0]
    prev_count = 1

    for d in temp[1:]:
        if d == prev:
            prev_count += 1
            max_count = max(max_count,prev_count)
        else:
            prev = d
            prev_count = 1
    answer = max(answer,max_count)

print(answer)
