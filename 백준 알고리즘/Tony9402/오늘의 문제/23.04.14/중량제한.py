# [BOJ] 1939
# LEVEL : G3

import sys
import heapq
from collections import deque


n,m = map(int,sys.stdin.readline().rstrip().split())

data = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    data[a].append((b,c))


starts, end = map(int,sys.stdin.readline().rstrip().split())


for i in range(1, n + 1):
    data[i].sort(reverse=True)

def bfs(start,ans):
    global end,n
    q = deque()

    visited[start] = True
    for next, cost in data[a]:
        if cost >= ans:
            q.append((next,cost))
            visited[next] = True

    while q:
        v,c = q.popleft()
        if v == end:
            return True
        else:
            for nex,co in data[v]:
                if not visited[nex] and co >= ans:
                    q.append((nex,co))
                    visited[nex] = True
    return False



cost_start = 0
cost_end = int(1e9)

while cost_start <= cost_end:
    visited = [False] * (n+1)
    mid = cost_start + (cost_end-cost_start)//2

    if bfs(starts,mid):
        start = mid + 1
    else:
        end = mid - 1

print(cost_end)








#
# q = []
# hm = {}
#
# for i in range(m):
#     a,b,c = map(int,sys.stdin.readline().rstrip().split())
#
#     if hm.get(a):
#         if hm[a].get(b):
#             if hm[a][b] > c:
#                 hm[a][b] = c
#         else:
#             hm[a][b] = c
#     else:
#         hm[a] = {b:c}
#
#     if hm.get(b):
#         if hm[b].get(a):
#             if hm[b][a] > c:
#                 hm[b][a] = c
#         else:
#             hm[b][a] = c
#     else:
#         hm[b] = {a:c}
#
# start, end = map(int,sys.stdin.readline().rstrip().split())
#
# answer = [int(1e9)] * (n+1)
#
# for v,c in hm[start].items():
#     heapq.heappush(q, (-c, v, start))
#     answer[v] = c
# # visited[start] = True
#
# while q:
#     cost,next,prev = heapq.heappop(q)
#     cost = -cost
#     for v, c in hm[next].items():
#         temp = min(answer[next], c)
#         if answer[v] == int(1e9) or answer[v] < temp:
#             heapq.heappush(q, (-temp, v, next))
#             answer[v] = temp
# print(answer[end])


