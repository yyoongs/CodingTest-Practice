# [BOJ] 1301
# LEVEL : G3
# 시간초과

import sys

n = int(sys.stdin.readline().rstrip())

bizz = [[0]*11 for _ in range(7)]

data = [0] * 5
for i in range(n):
    data[i] = int(sys.stdin.readline().rstrip())

answer = 0


def counts(pprev,prev, a,b,c,d,e):
    global answer
    temp = 0
    if a == 0 and b ==0 and c ==0 and d == 0:
        return 1

    if prev == -1:
        if a > 0:
            temp += counts(-1,1,a-1,b,c,d,e)
        if b > 0:
            temp += counts(-1, 2, a , b-1, c, d, e)
        if c > 0:
            temp += counts(-1, 3, a , b, c-1, d, e)
        if d > 0:
            temp += counts(-1, 4, a , b, c, d-1, e)
        if e > 0:
            temp += counts(-1, 5, a , b, c, d, e-1)

    elif pprev == -1:
        if a > 0 and prev != 1:
            temp += counts(prev,1,a-1,b,c,d,e)
        if b > 0 and prev != 2:
            temp += counts(prev, 2, a , b-1, c, d, e)
        if c > 0 and prev != 3:
            temp += counts(prev, 3, a , b, c-1, d, e)
        if d > 0 and prev != 4:
            temp += counts(prev, 4, a , b, c, d-1, e)
        if e > 0 and prev != 5:
            temp += counts(prev, 5, a , b, c, d, e-1)
    else:
        if a > 0 and prev != 1 and pprev != 1:
            temp += counts(prev,1,a-1,b,c,d,e)
        if b > 0 and prev != 2 and pprev != 2:
            temp += counts(prev, 2, a , b-1, c, d, e)
        if c > 0 and prev != 3 and pprev != 3:
            temp += counts(prev, 3, a , b, c-1, d, e)
        if d > 0 and prev != 4 and pprev != 4:
            temp += counts(prev, 4, a , b, c, d-1, e)
        if e > 0 and prev != 5 and pprev != 5:
            temp += counts(prev, 5, a , b, c, d, e-1)
    return temp

print(counts(-1,-1,data[0],data[1],data[2],data[3],data[4]))
