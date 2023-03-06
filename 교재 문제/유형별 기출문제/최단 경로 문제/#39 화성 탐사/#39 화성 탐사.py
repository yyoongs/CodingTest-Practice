import heapq

n = int(input())

graph = []
# graph = [[5, 5, 4], [3, 9, 1], [3, 2, 7]]
# n = 3
for i in range(n):
    graph.append(list(map(int,input().split())))


inf = int(1e9)
distance = [[inf]*(n) for _ in range(n)]

q = []
distance[0][0] = 5

dx = [0,-1,0,1]
dy = [1,0,-1,0]



def dijsktra(x,y):
    heapq.heappush(q,(graph[x][y],x,y))

    while q:
        dis, vx, vy = heapq.heappop(q)
        if distance[vx][vy] >= dis:
            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if distance[nx][ny] > dis + graph[nx][ny]:
                        heapq.heappush(q, (dis + graph[nx][ny], nx, ny))
                        distance[nx][ny] = dis + graph[nx][ny]

dijsktra(0,0)

print(distance[-1][-1])
