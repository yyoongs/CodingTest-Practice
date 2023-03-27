def solution(rows, columns, queries):
    answer = []
    maps = [[0] * (columns + 1) for _ in range(rows + 1)]
    n = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            maps[i][j] = n
            n += 1

    def rotate(s1, s2, e1, e2):
        mins = int(1e9)
        temp1 = maps[s1][s2]
        mins = min(mins, temp1)
        for i in range(s1 + 1, e1 + 1):
            maps[i - 1][s2] = maps[i][s2]
            mins = min(mins, maps[i - 1][s2])
        for j in range(s2 + 1, e2 + 1):
            maps[e1][j - 1] = maps[e1][j]
            mins = min(mins, maps[e1][j - 1])
        for k in range(e1, s1, -1):
            maps[k][e2] = maps[k - 1][e2]
            mins = min(mins, maps[k][e2])
        for l in range(e2, s2 + 1, -1):
            maps[s1][l] = maps[s1][l - 1]
            mins = min(mins, maps[s1][l])
        maps[s1][s2 + 1] = temp1
        return mins

    for sx, sy, ex, ey in queries:
        answer.append(rotate(sx, sy, ex, ey))

    return answer