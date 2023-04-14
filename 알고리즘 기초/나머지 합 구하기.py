# BOJ 10986
# LEVEL : G3

n,m = map(int,input().split())

data = [0] + list(map(int,input().split()))
sums = [0] * (len(data)+1)
count = 0
remains = [0] * m
for i in range(1,n+1):
    sums[i] = sums[i-1] + data[i]

for idx,s in enumerate(sums):
    sums[idx] = sums[idx] % m
    if idx not in [0,len(sums)-1]:
        if sums[idx] == 0:
            count += 1

        remains[sums[idx]] += 1

for r in remains:
    count += r*(r-1) // 2

print(count)