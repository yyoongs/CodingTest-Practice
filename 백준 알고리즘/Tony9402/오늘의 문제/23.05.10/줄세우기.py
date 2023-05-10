# [BOJ] 2631
# LEVEL : G4

# 7
# 3
# 7
# 5
# 2
# 6
# 1
# 4
import sys
input = sys.stdin.readline

n = int(input())

d = [1]*(n+1)
num = [0]
for i in range(n):
    num.append(int(input()))

for i in range(1,n+1):
    for j in range(1,i):
        if num[j]<num[i]:
            d[i]=max(d[i],d[j]+1)

print(d)

print(n-max(d))