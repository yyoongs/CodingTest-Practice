# [BOJ] 1003
# LEVEL : S3


import sys

# 3
# 0
# 1
# 3

n = int(sys.stdin.readline().rstrip())
dp = [[0] * 2 for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1


for j in range(3,41):
    dp[j][0] = dp[j-1][0] + dp[j-2][0]
    dp[j][1] = dp[j-1][1] + dp[j-2][1]

for i in range(n):
    target = int(sys.stdin.readline().rstrip())
    print(f"{dp[target][0]} {dp[target][1]}")
