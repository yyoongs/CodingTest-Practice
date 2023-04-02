import sys

n, l, r = map(int,sys.stdin.readline().rstrip().split())

maps = []

for i in range(n):
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    maps.append(line)


n,l,r = 2,20,50
maps = [[50,30],[30,40]]

n,l,r = 3,5,10
maps = [[10, 15, 20], [20, 30,25], [40,22,10]]

n,l,r = 4,10,50
maps = [[10, 100, 20,90], [80,100, 60,70], [70,20,30,40],[50,20,100,10]]


visited = [[False] * n for _ in range(n)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
temp = []
sums = 0

def dfs(x,y):
    if visited[x][y] == True:
        return
    else:
        global sums
        q = []
        temp.append((x,y))
        sums += maps[x][y]
        q.append((x,y))
        visited[x][y] = True
        while q:
            cx,cy = q.pop()

            for d_x,d_y in zip(dx,dy):
                nx = cx + d_x
                ny = cy + d_y
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and not visited[nx][ny] and l <= abs(maps[cx][cy] - maps[nx][ny]) <= r:
                    temp.append((nx,ny))
                    sums += maps[nx][ny]
                    visited[nx][ny] = True
                    q.append((nx,ny))

day = 1
flag = False
while True:
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = []
            sums = 0
            dfs(i,j)
            if len(temp) >= 2:
                flag = True
            for x,y in temp:
                maps[x][y] = sums//len(temp)

    if not flag:
        print(day-1)
        break
    else:
        day += 1
        flag = False
