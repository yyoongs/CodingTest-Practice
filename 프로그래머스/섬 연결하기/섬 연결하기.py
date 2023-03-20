import heapq


def solution(n, costs):
    answer = 0
    nodes = [[] for _ in range(n)]

    print(nodes)
    costs = sorted(costs, key=lambda x: x[2])
    print(costs)
    for s, d, c in costs:
        nodes[s].append([s, d, c])
    print(nodes)

    q = []

    heapq.heappush(q, (costs[0][2], costs[0][0], costs[0][1]))

    visited = [False] * n
    print(visited)
    while q:
        v = heapq.heappop(q)
        print(v, answer, visited)
        print(visited[v[1]], visited[v[2]])
        if visited[v[1]] and visited[v[2]]:
            continue
        else:
            if not visited[v[1]]:
                visited[v[1]] = True
                for i in range(len(nodes[v[1]])):
                    heapq.heappush(q, (nodes[v[1]][i][2], nodes[v[1]][i][0], nodes[v[1]][i][1]))
            if not visited[v[2]]:
                visited[v[2]] = True
                for i in range(len(nodes[v[2]])):
                    heapq.heappush(q, (nodes[v[2]][i][2], nodes[v[2]][i][0], nodes[v[2]][i][1]))
            answer += v[0]

    return answer