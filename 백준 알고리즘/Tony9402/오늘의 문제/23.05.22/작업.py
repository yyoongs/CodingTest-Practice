# [BOJ] 2056
# LEVEL : G4

# 7
# 5 0
# 1 1 1
# 3 1 2
# 6 1 1
# 1 2 2 4
# 8 2 2 4
# 4 3 3 5 6
import sys

n = int(sys.stdin.readline().rstrip())

hm = {}
dp = [0] * (n+1)
for i in range(n):
    duration, *pre = map(int,sys.stdin.readline().rstrip().split())
    hm[i+1] = [duration,pre[1:]]

for j in range(1,n+1):
    if len(hm[j][1]) == 0:
        dp[j] = hm[j][0]
    else:
        for k in hm[j][1]:
            dp[j] = max(dp[k]+hm[j][0], dp[j])

print(max(dp))

