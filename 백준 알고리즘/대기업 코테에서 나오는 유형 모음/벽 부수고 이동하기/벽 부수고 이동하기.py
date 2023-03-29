import sys
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split())
maps = [[0]*(m+1)]

for i in range(n):
    inputs = sys.stdin.readline().rstrip()
    line = [0]
    for c in inputs:
        line.append(int(c))
    maps.append(line)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    count = 1
    use = 0
    visited = [[[False] * (m + 1) for _ in range(n + 1)] for _ in range(2)]
    q = deque()
    q.append([1, 1, count, use])
    visited[0][1][1] = True
    while q:
        cx, cy, cost, use = q.popleft()
        if cx == n and cy == m:
            return cost
        cost += 1
        for x, y in zip(dx, dy):
            nx, ny = cx + x, cy + y
            if 1 <= nx <= n and 1 <= ny <= m and not visited[use][nx][ny]:
                if maps[nx][ny] == 0:
                    q.append([nx, ny, cost, use])
                    visited[use][nx][ny] = True
                if maps[nx][ny] == 1 and use == 0:
                    q.append([nx, ny, cost, 1])
                    visited[1][nx][ny] = True
    return -1


print(bfs())