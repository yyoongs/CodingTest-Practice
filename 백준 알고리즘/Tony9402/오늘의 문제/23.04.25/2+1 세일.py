# [BOJ] 11508
# LEVEL : S4

import sys

n = int(sys.stdin.readline().rstrip())

data = []

for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    data.append(temp)


data.sort(reverse=True)

answer = 0

for j in range(n):
    if j % 3 == 2:
        continue
    else:
        answer += data[j]

print(answer)