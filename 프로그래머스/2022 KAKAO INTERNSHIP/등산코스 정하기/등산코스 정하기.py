import heapq


def solution(n, paths, gates, summits):
    result = [0, int(1e9)]
    maps = [[] for _ in range(n + 1)]
    for s, e, c in paths:
        maps[s].append((e, c))
        maps[e].append((s, c))

    answer = [int(1e9)] * (n + 1)
    visited = [False] * (n + 1)
    q = []
    for start in gates:
        heapq.heappush(q, (0, start))

    while q:
        cost, v = heapq.heappop(q)
        answer[v] = min(cost, answer[v])
        if not visited[v]:
            if v in summits:
                visited[v] = True
                continue
            else:
                for i in range(len(maps[v])):
                    heapq.heappush(q, (max(maps[v][i][1], cost), maps[v][i][0]))
                    visited[v] = True

    for i in summits:
        if result[1] > answer[i]:
            result = [i, answer[i]]
        elif result[1] == answer[i]:
            if i < result[0]:
                result = [i, answer[i]]

    return result