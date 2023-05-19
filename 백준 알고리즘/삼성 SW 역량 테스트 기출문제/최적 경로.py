import sys

INF = sys.maxsize

n = int(input())
data = list(map(int, input().split()))
company = (data[0], data[1])
home = (data[2], data[3])
nodes = []
for i in range(n):
    nodes.append((i, data[i * 2 + 4], data[i * 2 + 5]))
# print(node)
answer = INF
visited = [0] * n


def dfs(x, y, ans):
    global answer
    if sum(visited) == n:
        answer = min(answer, ans + abs(home[0] - x) + abs(home[1] - y))
        return
    else:
        for node in nodes:
            if not visited[node[0]]:
                visited[node[0]] = 1
                dfs(node[1], node[2], ans + abs(node[1] - x) + abs(node[2] - y))
                visited[node[0]] = 0


dfs(company[0], company[1], 0)
print(answer)