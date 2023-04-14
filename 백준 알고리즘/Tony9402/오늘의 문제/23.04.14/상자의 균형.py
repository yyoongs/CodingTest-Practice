# [BOJ] 20116
# LEVEL : S3

import sys

n,l = map(int,sys.stdin.readline().rstrip().split())

data = list(map(int,sys.stdin.readline().rstrip().split()))
count = 1
flag = True
while len(data) != 1:
    last = data.pop()
    prev = data.pop()

    if prev-l < last/count < prev +l:
        sums = last + prev
        data.append(sums)
        count += 1
        continue
    else:
        flag = False
        print('unstable')
        break

if flag:
    print('stable')


