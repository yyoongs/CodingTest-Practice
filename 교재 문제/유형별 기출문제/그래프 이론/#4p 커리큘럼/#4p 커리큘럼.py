from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
cost = [0]
for i in range(n):
    temp = list(map(int,input().split()))
    for idx, t in enumerate(temp):
        if t != -1:
            if idx == 0:
                cost.append(t)
            else:
                graph[i].append(t)


print(graph)
print(cost)

graph = [[], [], [1], [1],[1, 3], [3]]
cost = [0, 10, 10, 4, 4, 3]
result = [0, 10, 10, 4, 4, 3]

q = deque()
degree = [999,0,1,1,2,1]
for idx, i in enumerate(degree):
    if idx == 0:
        pass
    if i == 0:
        q.append(idx)
        print(idx)

while q:
    current_idx = q.popleft()
    for next_idx, g in enumerate(graph):
        if next_idx != current_idx:
            if current_idx in g:
                result[next_idx] = max(result[next_idx], result[current_idx] + cost[next_idx])
                # g.remove(current_idx)
                degree[next_idx] -=1

            if degree[next_idx] == 0:
                q.append(next_idx)


print(graph)
print(result)
