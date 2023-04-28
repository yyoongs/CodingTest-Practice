# [BOJ] 17144
# LEVEL : G4
#
# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0

import sys


r,c,t = map(int,sys.stdin.readline().rstrip().split())

maps = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def spread():
    temp = [[0]*c for _ in range(r)]
    for a in range(r):
        for b in range(c):
            if maps[a][b] not in [0,-1]:
                amount = maps[a][b] // 5
                for x,y in zip(dx,dy):
                    nx = a+x
                    ny = b+y
                    if 0<=nx<r and 0<=ny<c and maps[nx][ny] != -1:
                        temp[nx][ny] += amount
                        maps[a][b] -= amount
    for d in range(r):
        for e in range(c):
            maps[d][e] += temp[d][e]


def air_conditioning():
    loc = []

    for f in range(r):
        if maps[f][0] == -1:
            loc.append(f)
    # print(loc)
    # maps[loc[0]-1][0] = 0
    for f in range(loc[0]-2,-1,-1):
        maps[f+1][0] = maps[f][0]
    for g in range(1,c):
        maps[0][g-1] = maps[0][g]
    for h in range(1,loc[0]+1):
        maps[h-1][c-1] = maps[h][c-1]
    for i in range(c-2,0,-1):
        maps[loc[0]][i+1] = maps[loc[0]][i]
    maps[loc[0]][1] = 0

    # maps[loc[1] + 1][0] = 0
    for h in range(loc[1]+2,r):
        maps[h-1][0] = maps[h][0]
    for g in range(1,c):
        maps[r-1][g-1] = maps[r-1][g]
    for f in range(r-2,loc[1]-1,-1):
        maps[f+1][c-1] = maps[f][c-1]
    for i in range(c-2,0,-1):
        maps[loc[1]][i+1] = maps[loc[1]][i]
    maps[loc[1]][1] = 0

def counting():
    answer = 0
    for d in range(r):
        for e in range(c):
            answer += maps[d][e]
    print(answer+2)

for i in range(r):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    maps.append(line)
# r,c,t = 7,8,1
# print(maps)
# maps = [[0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 0, 0, 3, 0, 0, 8], [-1, 0, 5, 0, 0, 0, 22, 0], [-1, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 10, 43, 0], [0, 0, 5, 0, 15, 0, 0, 0], [0, 0, 40, 0, 0, 0, 20, 0]]
# counting()
#
#
#
# counting()
for tries in range(t):

    spread()

    air_conditioning()
counting()
# print(sum(maps))