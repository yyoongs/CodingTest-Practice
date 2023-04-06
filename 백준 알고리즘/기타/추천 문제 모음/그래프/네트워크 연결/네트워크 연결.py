import sys

n = int(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph.append((c,a,b))


graph.sort()


def find(x):
    if val[x] != x:
        return find(val[x])
    else:
        return x


def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        val[y] = val[x]
    else:
        val[x] = val[y]
    return


val = [ i for i in range(n+1)]

cost = 0
for c,a,b in graph:
    if find(a) != find(b):
        cost += c
        union(a,b)

print(cost)
