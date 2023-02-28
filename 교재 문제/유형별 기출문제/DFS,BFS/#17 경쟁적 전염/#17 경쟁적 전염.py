
from collections import deque

n, k = map(int,input().split())

data = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    data[i+1] = [0] + list(map(int,input().split()))

s,x,y = map(int, input().split())

ti = 0
virus = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def find_virus(n):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == n:
                virus.append([n,(i,j)])


for i in range(k+1):
    find_virus(i+1)

virus.sort(key=lambda x:x[0])


def dfs(a,b):
    global ti

    q = deque(virus)

    while q:

        if ti == s:
            return data[a][b]

        n, now = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 1 or nx >=len(data) or ny < 1 or ny >= len(data) or data[nx][ny] != 0:
                continue
            else:
                data[nx][ny] = n
                q.append([n,(nx,ny)])

        if n == k:
            ti += 1

print(dfs(x,y))
print(data)

