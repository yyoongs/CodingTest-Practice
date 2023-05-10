# [BOJ] 1937
# LEVEL : G3


import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().rstrip())

maps = []

for i in range(n):
    li = list(map(int,sys.stdin.readline().rstrip().split()))
    maps.append(li)

# print(maps)
#
# n = 4
# maps = [[14, 9, 12, 10], [1, 11, 5, 4], [7, 15, 2, 13], [6, 3, 16, 8]]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0
answers = [[0] * n for _ in range(n)]


def dfs(posx,posy):
    global n
    if answers[posx][posy] != 0:
        return answers[posx][posy]
    answers[posx][posy] = 1
    for x,y in zip(dx,dy):
        nx = posx + x
        ny = posy + y
        if 0<=nx<n and 0<=ny<n and maps[posx][posy] < maps[nx][ny]:
            answers[posx][posy] = max(answers[posx][posy], dfs(nx,ny)+1)
    return answers[posx][posy]


for a in range(n):
    for b in range(n):
        answer = max(answer,dfs(a,b))

print(answer)


# dfs / back tracking
# import sys
#
# n = int(sys.stdin.readline().rstrip())
#
# maps = []
#
# for i in range(n):
#     li = list(map(int,sys.stdin.readline().rstrip().split()))
#     maps.append(li)
# print(maps)
#
# n = 4
# maps = [[14, 9, 12, 10], [1, 11, 5, 4], [7, 15, 2, 13], [6, 3, 16, 8]]
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
#
# answer = 0
# visited = [[False] * n for _ in range(n)]
#
#
# def dfs(posx,posy,count):
#     global answer
#     answer = max(answer,count)
#
#     for x,y in zip(dx,dy):
#         nx = posx + x
#         ny = posy + y
#         if 0<=nx<n and 0<=ny<n and maps[posx][posy] < maps[nx][ny]:
#             visited[nx][ny] = True
#             dfs(nx,ny,count+1)
#             visited[nx][ny] = False
#     return
#
#
# for a in range(n):
#     for b in range(n):
#         visited = [[False] * n for _ in range(n)]
#         visited[a][b] = True
#         dfs(a,b,1)
#
# print(answer)
