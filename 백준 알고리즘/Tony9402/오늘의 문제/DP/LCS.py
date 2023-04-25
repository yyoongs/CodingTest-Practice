# [BOJ] 9251
# LEVEL : G5


# ACAYKP
# CAPCAK
# C 0 1 1 1 1 1
# a 1 1 2 2 2 2
# p 1 1 2 2 2 3
# c 1 2 2 2 2 2
# a 1 2 3 3 3 3
# k 1 2 3 3 4 4


import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
answer = 0
for a in range(1,len(s1)+1):
    for b in range(1,len(s2)+1):
        if s1[a-1] == s2[b-1]:
            dp[b][a] = dp[b-1][a-1] + 1

        else:
            dp[b][a] = max(dp[b-1][a],dp[b][a-1])

        answer = max(answer, dp[b][a])
print(answer)
