# [BOJ] 11659
# LEVEL : S3

n,m = map(int,input().split())

data = [0] + list(map(int,input().split()))
sums = [0] * (len(data)+1)
for i in range(1,len(data)):
    sums[i] = sums[i-1] + data[i]


for i in range(m):
    s,e = map(int,input().split())
    print(sums[e]-sums[s-1])

