# [BOJ] 11062
# LEVEL : G3

# 2
# 4
# 1 2 5 2
# 9
# 1 1 1 1 2 2 2 2 2

# 1 가져갔을 때 -> 1 + dp 2 5 2
# 2 가져갔을 때 -> 2 + dp 1 2 5

# 1 2 6 6 14 16
# 0 2 5 4 15 12
# 0 0 5 5 12 15
# 0 0 0 2 10 10
# 0 0 0 0 10 10
# 0 0 0 0 00 08
# 2
# 1 2
# 2 5
# 5
# 5 2
# 5

# n = 6
# cards = [1, 2, 5, 2, 10, 8]
# dp = [[0] * 6 for _ in range(6)]
#
# n = 9
# cards = [1, 1, 1, 1, 2, 2, 2,2,2]
# dp = [[0] * 9 for _ in range(9)]

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cards = list(map(int,sys.stdin.readline().rstrip().split()))


    dp = [[0] * n for _ in range(n)]
    sums = []
    temp = 0
    for i in range(n):
        temp += cards[i]
        sums.append(temp)
        dp[i][i] = cards[i]
    #
    # print(dp)
    # print(sums)
    for i in range(1,n):
        for j in range(n-i):
            if j == 0:
                array_sum = sums[j+i]
            else:
                array_sum = sums[j+i] - sums[j-1]
            dp[j][j+i] = array_sum - min(dp[j+1][j+i], dp[j][j+i-1])
    # print(dp)
    print(dp[0][-1])