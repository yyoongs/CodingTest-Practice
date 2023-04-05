import sys

n = int(sys.stdin.readline().rstrip())

data = list(map(int,sys.stdin.readline().rstrip().split()))

result = [0] + [int(1e9)] * (n-1)

for i in range(n):
    jump = data[i]
    for j in range(1,jump+1):
        if i+j < n:
            result[i+j] = min(result[i] + 1, result[i+j])

if result[-1] == int(1e9):
    print(-1)
else:
    print(result[-1])
