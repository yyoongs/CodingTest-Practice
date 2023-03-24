from collections import deque


def solution(n, edge):
    answer = 0
    visited = ["F"] * (n + 1)
    edges = [[] for _ in range(n + 1)]
    for a, b in edge:
        edges[a].append(b)
        edges[b].append(a)

    def bfs():
        q = deque()
        q.append(1)
        visited[1] = 0
        while q:
            v = q.popleft()
            for i in edges[v]:
                if visited[i] == "F":
                    visited[i] = visited[v] + 1
                    q.append(i)

    bfs()

    answer = visited.count(max(visited[1:]))

    return answer