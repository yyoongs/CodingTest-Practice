n = int(input())

m = int(input())

# nodes = [[] for _ in range (n+1)]
inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for i in range(m):
    routes = list(map(int, input().split()))
    if routes[2] < graph[routes[0]][routes[1]]:
        graph[routes[0]][routes[1]] = routes[2]

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for _ in range(1,n+1):
    print(graph[_][1:])