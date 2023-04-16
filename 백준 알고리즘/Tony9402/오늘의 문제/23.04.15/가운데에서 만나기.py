import sys
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split())
maps = [[int(1e9)] *(n+1) for _ in range(n+1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            maps[a][b] = 0
for i in range(m):
    s,e,c = map(int,sys.stdin.readline().rstrip().split())
    maps[s][e] = c

routes = [[int(1e9)] * (n+1) for _ in range(n+1)]
#
# def bfs(start):
#     global n,m
#     q = deque()
#     routes[start][start] = 0
#     answers = [int(1e9)] * (n+1)
#     answers[start] = 0
#     for e,c in maps[start]:
#         q.append((e,c,start))
#
#     while q:
#         next,cost,prev = q.popleft()
#         answers[next] = answers[prev] + cost
#
#         for end,co in maps[next]:
#             if answers[end] > answers[next] + co:
#                 q.append((end,co,next))
#
#     for i in range(1,n+1):
#         routes[start][i] = answers[i]
#
#
k = int(sys.stdin.readline().rstrip())
person = list(map(int,sys.stdin.readline().rstrip().split()))
#
# for i in range(1,n+1):
#     bfs(i)


for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            maps[a][b] = min(maps[a][b],maps[a][i] + maps[i][b])


max_costs = int(1e9)
answer = []
for k in range(1,n+1):
    flag = False
    temp_costs = 0
    for p in person:
        if maps[p][k] != int(1e9) and maps[k][p] != int(1e9):
            costs = maps[p][k] + maps[k][p]
            temp_costs = max(costs, temp_costs)
        else:
            flag = True
            break

    if flag:
        continue
    else:
        if max_costs > temp_costs:
            max_costs = temp_costs
            answer = [k]
        elif max_costs == temp_costs:
            answer.append(k)


for ans in answer:
    print(ans,end=" ")
