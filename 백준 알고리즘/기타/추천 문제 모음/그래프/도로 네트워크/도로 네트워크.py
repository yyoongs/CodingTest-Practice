import sys
import heapq

n = int(sys.stdin.readline().rstrip())

roads = [[0] * (n+1) for _ in range(n+1)]
for i in range(n-1):
    s,e,cost = map(int,sys.stdin.readline().rstrip().split())
    roads[s][e] = cost
    roads[e][s] = cost
print(roads)
def dijkstra(start,end):
    visited = [False] * (n+1)
    answer = [int(1e9)] * (n+1)
    q = []
    visited[start] = True
    answer[start] = 0
    for idx in range(n+1):
        if roads[start][idx] != 0:
            heapq.heappush(q,(roads[start][idx],idx))
            answer[idx] = min(answer[idx],roads[start][idx])
    while q:
        cost, node = heapq.heappop(q)
        visited[node] = True
        for idx in range(n + 1):
            if roads[node][idx] != 0 and not visited[idx]:
                if cost + roads[node][idx] < answer[idx]:
                    heapq.heappush(q, (cost + roads[node][idx], idx))
                    answer[idx] = cost + roads[node][idx]
    print(visited)
    print(answer)
    return answer

k = int(sys.stdin.readline().rstrip())

for i in range(k):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    print(dijkstra(s,e))

