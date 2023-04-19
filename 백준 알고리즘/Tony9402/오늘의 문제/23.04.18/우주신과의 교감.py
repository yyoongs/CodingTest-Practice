# [BOJ] 1774
# LEVEL : G3

#empl1
# 4 1
# 1 1
# 3 1
# 2 3
# 4 3
# 1 4

import sys
import heapq


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    nx = find(x)
    ny = find(y)

    if nx == ny:
        return
    elif nx < ny:
        parent[ny] = nx
    else:
        parent[nx] = ny

    return


n,m = map(int,sys.stdin.readline().rstrip().split())

parent = [ i for i in range(n+1)]
pos = []

for _ in range(n):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    pos.append([x,y])

for _ in range(m):
    c, d = map(int, sys.stdin.readline().rstrip().split())
    if find(c) != find(d):
        union(c,d)


q = []

for a in range(n):
    for b in range(n):
        if a!=b:
            dis = pow(pow(abs(pos[a][1] - pos[b][1]),2) + pow(abs(pos[a][0] - pos[b][0]) , 2), 0.5)
            heapq.heappush(q,(round(dis,2),a+1,b+1))


answer = 0

while q:
    d,s,e = heapq.heappop(q)
    if find(s) != find(e):
        union(s,e)
        answer += d
    else:
        continue
print(parent)
print(format(answer,".2f"))


