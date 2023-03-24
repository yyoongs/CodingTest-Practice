def solution(m, n, puddles):
    answer = 1000000007
    maps = [['x'] * m for _ in range(n)]
    for x, y in puddles:
        maps[y - 1][x - 1] = 0
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                maps[i][j] = 1
            elif maps[i][j] == 0:
                continue
            elif i == 0 and j >= 1:
                maps[i][j] = maps[i][j - 1]
            elif j == 0:
                maps[i][j] = maps[i - 1][j]
            else:
                maps[i][j] = maps[i - 1][j] + maps[i][j - 1]

    return maps[-1][-1] % answer