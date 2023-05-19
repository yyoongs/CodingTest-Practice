# [BOJ] 2169
# LEVEL : G2

# 5 5
# 10 25 7 8 13
# 68 24 -78 63 32
# 12 -69 100 -29 -25
# -16 -22 -57 -33 99
# 7 -76 -11 77 15

import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
maps = []
for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    maps.append(temp)
# visited = [[False] * m for _ in range(n)]
dp = [[int(-1e9)] * m for _ in range(n)]

# n,m = 5,5
# print(maps)
# maps =  [[10, 25, 7, 8, 13], [68, 24, -78, 63, 32], [12, -69, 100, -29, -25], [-16, -22, -57, -33, 99], [7, -76, -11, 77, 15]]
#
# dx = [0,1,-1]
# dy = [1,0,0]
# visited[0][0] = True
#
# def dfs(posx,posy,cost):
#     if posx == m-1 and posy == n-1:
#         dp[-1][-1] = max(cost,dp[-1][-1])
#     else:
#         for ddx, ddy in zip(dx,dy):
#             cx = posx+ddx
#             cy = posy+ddy
#             print(cy,cx)
#             if 0<= cx <m and 0<= cy < n and not visited[cy][cx]:
#                 costs = cost+maps[cy][cx]
#                 if costs >= dp[cy][cx]:
#                     visited[cy][cx] = True
#                     dp[cy][cx] = costs
#                     dfs(cx,cy,costs)
#                     visited[cy][cx] = False
#
# dfs(0,0,maps[0][0])
dp[0][0] = maps[0][0]
for i in range(1,m):
    dp[0][i] = dp[0][i-1] + maps[0][i]

for j in range(1,n):
    left = [int(-1e9)] * m
    right = [int(-1e9)] * m

    dp[j][0] = dp[j-1][0] + maps[j][0]
    for i in range(m):
        if i == 0:
            left[0] = dp[j - 1][0] + maps[j][0]
        else:
            left[i] = max(dp[j-1][i] + maps[j][i], left[i-1] + maps[j][i])
    for i in range(m-1,-1,-1):
        if i == m-1:
            right[i] = dp[j - 1][i] + maps[j][i]
        else:
            right[i] = max(dp[j - 1][i] + maps[j][i], right[i + 1] + maps[j][i])
    for i in range(m):
        dp[j][i] = max(left[i],right[i])


print(dp[-1][-1])