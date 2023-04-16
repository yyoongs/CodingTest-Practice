# [BOJ] 1939
# LEVEL : G3

import sys
import heapq

n,m = map(int,sys.stdin.readline().rstrip().split())

q = []
hm = {}

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())

    if hm.get(a):
        if hm[a].get(b):
            if hm[a][b] > c:
                hm[a][b] = c
        else:
            hm[a][b] = c
    else:
        hm[a] = {b:c}

    if hm.get(b):
        if hm[b].get(a):
            if hm[b][a] > c:
                hm[b][a] = c
        else:
            hm[b][a] = c
    else:
        hm[b] = {a:c}

start, end = map(int,sys.stdin.readline().rstrip().split())

answer = [int(1e9)] * (n+1)

for v,c in hm[start].items():
    heapq.heappush(q, (-c, v, start))
    answer[v] = c
# visited[start] = True

while q:
    cost,next,prev = heapq.heappop(q)
    cost = -cost
    for v, c in hm[next].items():
        temp = min(answer[next], c)
        if answer[v] == int(1e9) or answer[v] < temp:
            heapq.heappush(q, (-temp, v, next))
            answer[v] = temp
print(answer[end])
