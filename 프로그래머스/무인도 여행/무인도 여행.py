import sys

sys.setrecursionlimit(10 ** 5)


def solution(maps):
    answer = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    def dfs(x, y):
        nonlocal cost
        if maps[x][y] == 'X' or visited[x][y] == True:
            return
        else:
            visited[x][y] = True
            cost += int(maps[x][y])
            for d_x, d_y in zip(dx, dy):
                nx = x + d_x
                ny = y + d_y
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    dfs(nx, ny)
                    visited[nx][ny] = True

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            cost = 0
            dfs(i, j)
            if cost != 0:
                answer.append(cost)

    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer