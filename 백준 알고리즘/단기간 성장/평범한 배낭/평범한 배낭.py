import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))

knapsack = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight, value = data.pop(0)
    for j in range(1,k+1):
        if weight <= j:
            knapsack[i][j] = max(knapsack[i-1][j],value + knapsack[i-1][j-weight])
        else:
            knapsack[i][j] = knapsack[i-1][j]

print(knapsack[n][k])
