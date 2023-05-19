import sys
import copy
sys.setrecursionlimit(100000)
r,c = map(int,sys.stdin.readline().rstrip().split())

maps = []

for i in range(r):
    maps.append(sys.stdin.readline().rstrip())

dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 0

def dfs(x,y,li,count):
    global answer
    answer = max(answer,count)

    for d_x, d_y in zip(dx,dy):
        nx = x + d_x
        ny = y + d_y
        if 0<=nx<r and 0<=ny<c and maps[nx][ny] not in li:
            temp = copy.deepcopy(li)
            temp.append(maps[nx][ny])
            dfs(nx,ny,temp,count+1)


dfs(0,0,[maps[0][0]],1)
print(answer)