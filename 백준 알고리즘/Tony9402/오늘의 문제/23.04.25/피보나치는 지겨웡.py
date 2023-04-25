# [BOJ] 17175
# LEVEL : S3

# 2

# 3
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

answer = 0

def find_count(n):
    if dp[n] == 0:
        dp[n] = find_count(n-1) + find_count(n-2) + 1

    return dp[n]

if n == 0:
    print(1)

elif n == 1:
    print(1)

elif n == 2:
    print(3)
else:
    dp[1] = 1
    dp[2] = 3
    answer = find_count(n)

    print(answer % 1000000007)
