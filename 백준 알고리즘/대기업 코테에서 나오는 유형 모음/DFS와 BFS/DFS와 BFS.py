from collections import deque
import sys

n,m,start = map(int,sys.stdin.readline().rstrip().split())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    edges[s].append(e)
    edges[e].append(s)

for i in range(len(edges)):
    edges[i].sort()

# n,m,start = 4,5,1
# edges = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]


# n,m,start = 5,5,3
# edges = [[], [2, 3], [1, 5], [1, 4], [3,5],[2, 4]]
#
#

def dfs(x):
    print(x, end=" ")
    for n in edges[x]:
        if not visited[n]:
            visited[n] = True
            dfs(n)


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        n = q.popleft()
        print(n,end=" ")
        for nex in edges[n]:
            if not visited[nex]:
                visited[nex] = True
                q.append(nex)


visited = [False] * (n+1)
visited[start] = True


dfs(start)
print()
visited = [False] * (n + 1)
visited[start] = True

bfs(start)