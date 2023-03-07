n, m = map(int,input().split())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i


def find_parent(x):
    if parent[x] != x:
        find_parent(parent[x])
    return parent[x]


def union_parent(x,y):
    tx = find_parent(x)
    ty = find_parent(y)

    if tx > ty :
        parent[x] = ty
    elif ty > tx:
        parent[y] = tx


edges = []

for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort(key=lambda x:x[0])

result = 0
last = 0
for c,a,b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result += c
        last = c

print(result - last)