# [BOJ] 1976
# LEVEL : G4

# 3
# 3
# 0 1 0
# 1 0 1
# 0 1 0
# 1 2 3

import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
maps = []
parent = [i for i in range(n)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x,y):
    dx = find(x)
    dy = find(y)

    if dx != dy:
        if dx < dy:
            parent[dy] = dx
        else:
            parent[dx] = dy
    return

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    maps.append(temp)

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            union(i,j)
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            union(i,j)

temp2 = list(map(int,sys.stdin.readline().rstrip().split()))

ans = parent[temp2[0]-1]
flag = True

for t in temp2[1:]:
    if find(t-1) != ans:
        print("NO")
        flag = False
        break

if flag:
    print("YES")
