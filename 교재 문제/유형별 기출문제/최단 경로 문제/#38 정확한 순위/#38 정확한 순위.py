n,m = map(int,input().split())
inf = int(1e9)
data = [[inf]*(n+1) for _ in range(n+1)]

for i in range(m):
    s,e = map(int,input().split())

    data[s][e] = 1

for i in range(n):
    data[i][i] = 0

print(data)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            data[a][b] = min(data[a][b],data[a][k]+data[k][b])


for i in range(1,n+1):
    print(data[i][1:])

result = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if data[i][j] != inf or data[j][i] != inf:
            count += 1

    if count == n:
        result += 1

print(result)