# [BOJ] 9536
# LEVEL : S4


import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    answer = ""
    sounds = list(sys.stdin.readline().rstrip().split())
    hm = {}

    while True:
        li = sys.stdin.readline().rstrip().split()
        if li[1] == 'does':
            break
        elif not hm.get(li[2]):
            hm[li[2]] = 1

    for s in sounds:
        if hm.get(s):
            continue
        else:
            answer += s + " "

    print(answer)