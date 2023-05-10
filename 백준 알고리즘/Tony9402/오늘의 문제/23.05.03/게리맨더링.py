# [BOJ] 17471
# LEVEL : G4

# 6
# 5 2 3 4 1 2
# 2 2 4
# 4 1 3 6 5
# 2 4 2
# 2 1 3
# 1 2
# 1 2

#6
# 1 1 1 1 1 1
# 2 2 4
# 4 1 3 6 5
# 2 4 2
# 2 1 3
# 1 2
# 1 2

# 6
# 2 3 4 5 6 7
# 2 2 3
# 2 1 3
# 2 1 2
# 2 5 6
# 2 4 6
# 2 4 5
from collections import deque
from itertools import combinations
import sys

INF = sys.maxsize
answer = int(INF)
n = int(sys.stdin.readline().rstrip())
#
values = [0] + list(map(int,sys.stdin.readline().rstrip().split()))

maps = [[] for _ in range(n+1)]

for i in range(n):
    l, *nexts = map(int,sys.stdin.readline().rstrip().split())
    for nex in nexts:
        maps[i+1].append(nex)

# values = [0] + [5, 2, 3, 4, 1, 2]
# maps = [[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]

vertexes = [i for i in range(1,n+1)]
def bfs(group):
    global n
    q = deque()
    q.append(group[0])
    visited = [True] + [False] * n
    visited[group[0]] = True
    for i in range(1,n+1):
        if i not in group:
            visited[i] = True
    while q:
        v = q.popleft()
        for nexx in maps[v]:
            if not visited[nexx]:
                q.append(nexx)
                visited[nexx] = True
    for v in range(len(visited)):
        if not visited[v]:
            return False
    return True

def sums(group):
    total = 0
    for g in group:
        total += values[g]
    return total


for i in range(1, n//2 +1):
    temp = combinations(vertexes,i)

    for t in temp:
        other = [i for i in vertexes if i not in t]
        if bfs(t) and bfs(other):
            answer = min(answer,abs(sums(t)-sums(other)))


if answer == int(INF):
    print(-1)
else:
    print(answer)


# 1 - 2
#   \ ㅣ
#     3

