from collections import deque


def solution(maps):
    data = []
    for l in maps:
        line = []
        for c in l:
            line.append(c)
        data.append(line)

    def bfs(x, y, cost, dest):
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
        visited = [[False] * len(data[0]) for _ in range(len(data))]
        q = deque()
        q.append((x, y, cost))
        visited[x][y] = True
        while q:
            cx, cy, cost = q.popleft()
            if data[cx][cy] == dest:
                return cx, cy, cost
            for d_x, d_y in zip(dx, dy):
                nx = cx + d_x
                ny = cy + d_y
                if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and (data[nx][ny] != 'X') and not visited[nx][ny]:
                    q.append((nx, ny, cost + 1))
                    visited[nx][ny] = True
        return -1, -1, -1

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "S":
                sx, sy, sc = bfs(i, j, 0, "L")
                if sc == -1:
                    return -1
                else:
                    return bfs(sx, sy, sc, "E")[2]
