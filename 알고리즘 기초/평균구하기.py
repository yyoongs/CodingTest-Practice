# [BOJ] 1546
# LEVEL:B1

n = int(input())

data = list(map(int,input().split()))
max_d = max(data)

print(sum(data) * 100 / max_d / len(data))