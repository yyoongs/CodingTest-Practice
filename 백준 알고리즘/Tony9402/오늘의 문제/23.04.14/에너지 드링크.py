# [BOJ] 20115
# LEVEL : S3

import sys
import heapq

n = int(sys.stdin.readline().rstrip())

data = list(map(int,sys.stdin.readline().rstrip().split()))

q = []

for d in data:
    heapq.heappush(q,-d)

while len(q) != 1:
    first = (-1) * heapq.heappop(q)
    second = (-1) * heapq.heappop(q)

    new_drink = (second / 2) + first

    heapq.heappush(q,-new_drink)

print(-heapq.heappop(q))

