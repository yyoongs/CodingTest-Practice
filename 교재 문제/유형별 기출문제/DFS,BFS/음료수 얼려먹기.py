import sys
from collections import deque

n, m = map(int,sys.stdin.readline().rstrip().split())

case = []

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    case.append(temp)

visited = [[False] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 0
# # BFS
# def bfs(posx,posy):
#     global answer
#     if case[posx][posy] == 0 and not visited[posx][posy]:
#         answer +=1
#
#     if case[posx][posy] == 1:
#         return
#
#     q = deque()
#     q.append([posx,posy])
#
#     while q:
#         cx, cy = q.popleft()
#
#         for x,y in zip(dx,dy):
#             nx = cx + x
#             ny = cy + y
#             if 0<= nx <n and 0<= ny < m and case[nx][ny] == 0 and not visited[nx][ny]:
#                 q.append([nx,ny])
#                 visited[nx][ny] = True
#
#
# for i in range(n):
#     for j in range(m):
#         bfs(i,j)
#
# print(answer)


# #2 dfs 재귀
# answer2 = 0
# visited2 = [[False] * m for _ in range(n)]
#
#
# def dfs(posx,posy):
#     if case[posx][posy] == 1:
#         return
#
#     for x, y in zip(dx, dy):
#         nx = posx + x
#         ny = posy + y
#         if 0 <= nx < n and 0 <= ny < m and case[nx][ny] == 0 and not visited2[nx][ny]:
#             visited2[nx][ny] = True
#             dfs(nx,ny)
#
# for i in range(n):
#     for j in range(m):
#         if case[i][j] == 0 and not visited2[i][j]:
#             answer2 += 1
#         dfs(i,j)
#
# print(answer2)

# #3 dfs 스택
# answer3 = 0
# visited3 = [[False] * m for _ in range(n)]
#
#
# def dfs(posx,posy):
#     if case[posx][posy] == 1 or visited3[posx][posy]:
#         return
#
#     q = []
#     q.append([posx,posy])
#     while q:
#         cx, cy = q.pop()
#         for x, y in zip(dx, dy):
#             nx = cx + x
#             ny = cy + y
#             if 0 <= nx < n and 0 <= ny < m and case[nx][ny] == 0 and not visited3[nx][ny]:
#                 visited3[nx][ny] = True
#                 q.append([nx,ny])
#
# for i in range(n):
#     for j in range(m):
#         if case[i][j] == 0 and not visited3[i][j]:
#             answer3 += 1
#         dfs(i,j)
#
# print(answer3)