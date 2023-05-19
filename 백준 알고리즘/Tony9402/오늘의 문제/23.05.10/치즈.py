# [BOJ] 2636
# LEVEL : G4

# 13 12
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 1 0 0 0
# 0 1 1 1 0 0 0 1 1 0 0 0
# 0 1 1 1 1 1 1 0 0 0 0 0
# 0 1 1 1 1 1 0 1 1 0 0 0
# 0 1 1 1 1 0 0 1 1 0 0 0
# 0 0 1 1 0 0 0 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0

import sys
sys.setrecursionlimit(10**5)
h,w = map(int,sys.stdin.readline().rstrip().split())
sums = 0

maps = []
#
for i in range(h):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    maps.append(temp)
    sums += sum(temp)

# print(maps)
# maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
#
#

def dfs(x, y):
    for ddx, ddy in zip(dx, dy):
        cx = x + ddx
        cy = y + ddy
        if 0 <= cx < h and 0 <= cy < w and not visited[cx][cy]:
            visited[cx][cy] = True
            if maps[cx][cy] == 0:
                dfs(cx, cy)
            else:
                temp.append((cx, cy))
    return

answer = 0
last = 0
while sums > 0:
    temp = []
    visited = [[False] * (w+1) for _ in range(h+1)]
    visited[0][0] = True
    dfs(0,0)
    sums -= len(temp)
    if sums == 0:
        last = len(temp)

    for sx,sy in temp:
        maps[sx][sy] = 0

    answer += 1
print(answer)
print(last)
