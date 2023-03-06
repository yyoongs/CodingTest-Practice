n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

idx = 0
for i in range(n):
    if i == 0:
        continue
    else:
        for idx in range(i+1):
            if idx == 0:
                data[i][idx] += data[i-1][idx]
            elif idx == i:
                data[i][idx] += data[i-1][idx-1]
            else:
                data[i][idx] = data[i][idx] + max(data[i-1][idx],data[i-1][idx-1])
max_value = 0
for idx in range(n):
    max_value = max(max_value,data[4][idx])

print(max_value)