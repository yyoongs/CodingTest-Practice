# [BOJ] 17396
# LEVEL : G5

# 5 7
# 0 0 0 1 1
# 0 1 7
# 0 2 2
# 1 2 4
# 1 3 3
# 1 4 6
# 2 3 2
# 3 4 1

import sys
import heapq
inf = sys.maxsize
n, m = map(int,sys.stdin.readline().rstrip().split())

maps = list(map(int,sys.stdin.readline().rstrip().split()))

path = [[] for _ in range(n)]

for i in range(m):
    s,e,c = map(int, sys.stdin.readline().rstrip().split())
    path[s].append((c,e))
    path[e].append((c,s))

# path = [[[7, 1], [2, 2]], [[7, 0], [4, 2], [3, 3], [6, 4]], [[2, 0], [4, 1], [2, 3]], [[3, 1], [2, 2], [1, 4]], [[6, 1], [1, 3]]]

distance = [inf] * n

distance[0] = 0
maps[-1] = 0
# print(path)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for ncost,nv in path[now]:
            # print(ncost,nv)
            cost = dist + ncost
            if cost < distance[nv] and maps[nv] == 0:
                distance[nv] = cost
                heapq.heappush(q,(cost,nv))

dijkstra(0)

if distance[-1] == inf:
    print(-1)
else:
    print(distance[-1])