# [BOJ] 18429
# LEVEL : S3

import sys
from itertools import permutations

n,k = map(int,sys.stdin.readline().rstrip().split())
data = list(map(int,sys.stdin.readline().rstrip().split()))
li = [i for i in range(n)]
permutation = list(permutations(li,n))

answer = 0
for p in permutation:
    temp = 500
    flag = True
    for idx in p:
        temp += data[idx]
        temp -= k
        if temp < 500:
            flag = False
            break
    if flag:
        answer += 1

print(answer)