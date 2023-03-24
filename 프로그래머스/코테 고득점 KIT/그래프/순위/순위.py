def solution(n, results):
    answer = 0
    res = [[None] * (n + 1) for _ in range(n + 1)]
    for w, l in results:
        res[w][l] = True
        res[l][w] = False

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if res[i][j] == None:
                    if res[i][k] == True and res[k][j] == True:
                        res[i][j] = True
                    if res[i][k] == False and res[k][j] == False:
                        res[i][j] = False

    for idx, g in enumerate(res[1:]):
        li = g[1:idx + 1] + g[idx + 2:]
        if li.count(None) == 0:
            answer += 1
    return answer