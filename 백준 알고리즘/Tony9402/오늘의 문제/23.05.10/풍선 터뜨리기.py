# [BOJ] 2346
# LEVEL : S3

# 5
# 3 2 1 -3 -1

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

data = list(map(int,sys.stdin.readline().rstrip().split()))

q = deque()

for idx, d in enumerate(data):
    q.append((idx+1,d))

result = []
while len(q) > 1:
    index, nums = q.popleft()
    result.append(index)
    if nums > 0:
        for i in range(nums-1):
            q.append(q.popleft())
    else:
        nums = abs(nums)
        for i in range(nums):
            q.insert(0,q.pop())
result.append(q[0][0])

for r in result:
    print(r,end=" ")
