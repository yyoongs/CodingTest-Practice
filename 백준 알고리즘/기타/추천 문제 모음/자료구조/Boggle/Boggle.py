import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
hashs = {}
score = {1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}
for i in range(n):
    string = sys.stdin.readline().rstrip()
    if hashs.get(len(string)):
        hashs[len(string)].append(string)
    else:
        hashs[len(string)] = [string]

space = input()

m = int(sys.stdin.readline().rstrip())


def bfs(x,y):
    visited = [[False] * 4 for _ in range(4)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    curr = ""
    length = 0
    global total, count, longest
    while q:
        cx,cy = q.popleft()
        curr += maps[cx][cy]
        print(curr)
        length += 1
        max_len = 0
        if hashs.get(length) and curr in hashs[length] and score.get(length):
            total += score[length]
            count += 1
            if length > max_len:
                max_len = length
                longest = [curr]
            elif length == max_len:
                longest.append(curr)

        for d_x,d_y in zip(dx,dy):
            nx = cx+d_x
            ny = cy+d_y
            if 0<=nx<4 and 0<=ny<4 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True





for i in range(m):
    maps = []
    for j in range(4):
        maps.append(sys.stdin.readline().rstrip())
    total = 0
    count = 0
    longest = []
    for a in range(4):
        for b in range(4):
            bfs(a,b)
    # print(maps[0][0])
    print(total,count,longest)
