# [BOJ] 15724
# LEVEL : S1

# 4 4
# 9 14 29 7
# 1 31 6 13
# 21 26 40 16
# 8 38 11 23
# 3
# 1 1 3 2
# 1 1 1 4
# 1 1 4 4

import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

maps = []

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    maps.append(temp)


dp = [[0]* (m+1) for _ in range(n+1)]
for a in range(1,m+1):
    for b in range(1,n+1):
        dp[b][a] =  dp[b-1][a] + dp[b][a-1] - dp[b-1][a-1] + maps[b-1][a-1]

print(dp)

k = int(sys.stdin.readline().rstrip())

for i in range(k):
    s1,s2,s3,s4 = map(int, sys.stdin.readline().rstrip().split())
    print(dp[s3][s4] - dp[s3][s2-1] - dp[s1-1][s4] + dp[s1-1][s2-1])



