# [BOJ] 5557
# LEVEL : G5

#empl1
# 11
# 8 3 2 4 8 7 2 4 0 8 8

#empl2
# 40
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1
import sys


# input = sys.stdin.readline

n = int(input())
count = 0
data = list(map(int,input().split()))

dp = [[0]*21 for _ in range(n)]

dp[0][data[0]] = 1
idx = 1
for d in data[1:-1]:
    for i in range(21):
        if dp[idx-1][i] > 0:
            if i + d <= 20:
                dp[idx][i+d] += dp[idx-1][i]
            if i - d >=0:
                dp[idx][i - d] += dp[idx - 1][i]
    idx+=1

print(dp[n-2][data[-1]])







#
# def dfs(answer,idx):
#     global n,count
#     if 0<=answer<=20:
#         if idx == n - 1:
#             if answer == data[-1]:
#                 count += 1
#                 return
#             else:
#                 return
#         else:
#             dfs(answer + data[idx], idx + 1)
#             dfs(answer - data[idx], idx + 1)
#
#     else:
#         return
#
#
# dfs(0,0)
#
# print(count)