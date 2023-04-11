import sys
from collections import deque

r,c = map(int,sys.stdin.readline().rstrip().split())
maps = []
for i in range(r):
    line = sys.stdin.readline().rstrip()
    temp = []
    for l in line:
        temp.append(l)
    maps.append(temp)


def bfs(sx,sy,waters):
    visited = [[False]* c for _ in range(r)]
    q = deque()
    turn = 0
    for wx,wy in waters:
        q.append([wx,wy,turn,'water'])
    q.append([sx,sy,turn,'char'])
    visited[sx][sy] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        cx,cy,turns,types = q.popleft()
        if maps[cx][cy] == 'D':

            return turns

        if types == 'water':
            for d_x,d_y in zip(dx,dy):
                nx = cx + d_x
                ny = cy + d_y
                if 0<=nx<r and 0<=ny<c and maps[nx][ny] not in ['X','D','*']:
                    q.append([nx,ny,turns+1,'water'])
                    maps[nx][ny] = '*'
        else:
            for d_x,d_y in zip(dx,dy):
                nx = cx + d_x
                ny = cy + d_y
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and maps[nx][ny] in ['.', 'D']:
                    q.append([nx,ny,turns+1,'char'])
                    visited[nx][ny] = True

    return 'KAKTUS'

pos_water = []
pos_char = []
for a in range(r):
    for b in range(c):
        if maps[a][b] == '*':
            pos_water.append([a,b])
        if maps[a][b] == 'S':
            pos_char = [a,b]

print(bfs(pos_char[0],pos_char[1],pos_water))
