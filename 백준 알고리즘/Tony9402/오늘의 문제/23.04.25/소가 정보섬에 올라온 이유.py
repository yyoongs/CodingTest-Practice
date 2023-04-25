# [BOJ] 17128
# LEVEL : S3

# 8 5
# -2 3 5 -6 10 -8 7 6
# 3 5 2 7 7

import sys

n, q = map(int,sys.stdin.readline().rstrip().split())


data = list(map(int,sys.stdin.readline().rstrip().split()))


data = data + data[:3]
answer = []

for i in range(n):
    answer.append(data[i] * data[i+1] * data[i+2] * data[i+3])

fun = list(map(int,sys.stdin.readline().rstrip().split()))

sums = sum(answer)

for i in range(q):
    for j in range(1,5):
        if fun[i]-j <0:
            answer[n+fun[i]-j] *= -1
            sums += 2*answer[n+fun[i]-j]
        else:
            answer[fun[i]-j] *= -1
            sums += 2*answer[fun[i]-j]
    print(sums)