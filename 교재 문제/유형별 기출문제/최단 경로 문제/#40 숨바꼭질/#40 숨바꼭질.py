import heapq

n, m = map(int,input().split())
inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]

distance = [inf] * (n+1)
distance[1] = 0
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

q = []

heapq.heappush(q,(0,1))

while q:
    dis, idx = heapq.heappop(q)
    if distance[idx] >= dis:
        for x in range(1,n+1):
            if graph[idx][x] == 1:
                if distance[x] >= dis+graph[idx][x]:
                    heapq.heappush(q,(dis+graph[idx][x],x))
                    distance[x] = dis+graph[idx][x]

max_val = max(distance[1:])
count = 0
li = []
for idx, val in enumerate(distance):
    if val == max_val:
        li.append(idx)
print(li[0])
print(max_val)
print(len(li))