# 재귀를 이용한 dfs -> 효율성 통과 x
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = n * m
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, count):
        nonlocal answer
        if x == m - 1 and y == n - 1:
            answer = min(answer, count)
        else:
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx]:
                    maps[y][x] = 0
                    dfs(nx, ny, count + 1)

    dfs(0, 0, 1)
    if answer == n * m:
        return -1
    return answer

#bfs
from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, -0, -1]

    q = deque()
    q.append([0, 0, 1])
    while q:
        cx, cy, count = q.popleft()
        if cx == m - 1 and cy == n - 1:
            return count

        for x, y in zip(dx, dy):
            nx = cx + x
            ny = cy + y
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                q.append([nx, ny, count + 1])
                maps[ny][nx] = count

    return -1
