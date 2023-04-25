# [BOJ] 9084
# LEVEL : G5


# 3
# 2
# 1 2
# 1000
# 3
# 1 5 10
# 100
# 2
# 5 7
# 22

import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())

    types = list(map(int,sys.stdin.readline().rstrip().split()))

    target = int(sys.stdin.readline().rstrip())

    dp = [0] * (target+1)
    dp[0] = 1

    for c in types:
        for j in range(1,target+1):
            if j - c >= 0:
                dp[j] += dp[j-c]

    print(dp[-1])