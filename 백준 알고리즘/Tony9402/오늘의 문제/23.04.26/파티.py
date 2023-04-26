# [BOJ] 1238
# LEVEL : G3

# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3

import sys
import heapq
# #
n, m, x = map(int,sys.stdin.readline().rstrip().split())

path = [[] for _ in range(n+1)]

for i in range(m):
    s,e,c = map(int,sys.stdin.readline().rstrip().split())
    path[s].append([c,e])

# n,m,x = 4,8,2
# path = [[], [[4, 2], [2, 3], [7, 4]], [[1, 1], [5, 3]], [[2, 1], [4, 4]], [[3, 2]]]

maps = [[int(1e9)] * (n+1) for _ in range(n+1)]

def dijkstra(start):
    q = []
    maps[start][start] = 0
    heapq.heappush(q,[0,start])

    while q:
        cost,now = heapq.heappop(q)
        if maps[start][now] < cost:
            continue

        for costs,next in path[now]:
            if maps[start][now] + costs < maps[start][next]:
                maps[start][next] = maps[start][now] + costs
                heapq.heappush(q, [costs,next])


for i in range(1,n+1):
    dijkstra(i)

max_time = 0

for i in range(1,n+1):
    if i!=x:
        max_time = max(max_time,maps[i][x] + maps[x][i])

print(max_time)


#2
n, m, x = map(int,sys.stdin.readline().rstrip().split())

path = [[] for _ in range(n+1)]
path2 = [[] for _ in range(n+1)]

for i in range(m):
    s,e,c = map(int,sys.stdin.readline().rstrip().split())
    path[s].append([c,e])
    path2[e].append([c,s])

maps = [int(1e9)] * (n+1)
maps2 = [int(1e9)] * (n+1)


def dijkstra(start):
    q = []
    maps[start] = 0
    heapq.heappush(q,[0,start])

    while q:
        cost,now = heapq.heappop(q)
        if maps[now] < cost:
            continue

        for costs,next in path[now]:
            if maps[now] + costs < maps[next]:
                maps[next] = maps[now] + costs
                heapq.heappush(q, [costs,next])


def dijkstra2(start):
    q = []
    maps2[start] = 0
    heapq.heappush(q,[0,start])

    while q:
        cost,now = heapq.heappop(q)
        if maps2[now] < cost:
            continue

        for costs,next in path2[now]:
            if maps2[now] + costs < maps2[next]:
                maps2[next] = maps2[now] + costs
                heapq.heappush(q, [costs,next])


dijkstra(x)
dijkstra2(x)
answer = 0
for i in range(1,n+1):
    if i != x:
        answer = max(answer,maps[i] + maps2[i])
print(answer)