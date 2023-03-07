n, m = map(int,input().split())

table = [0] * (n+1)

for i in range(n+1):
    table[i] = i

def find_parent(x):
    if table[x] != x:
        find_parent(table[x])
    return table[x]

def union_parent(a,b):
    ta = find_parent(a)
    tb = find_parent(b)

    if ta < tb:
        table[b] = a
    else:
        table[a] = b

result = []
for i in range(m):
    _type, a, b = map(int,input().split())

    if _type == 0:
        union_parent(a,b)
    else:
        check_a = find_parent(a)
        check_b = find_parent(b)

        if check_a == check_b:
            result.append("YES")
        else:
            result.append("NO")

for r in result:
    print(r)