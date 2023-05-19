# [BOJ] 2602
# LEVEL : G4

import sys

ans = sys.stdin.readline().rstrip()

devil = sys.stdin.readline().rstrip()
angel = sys.stdin.readline().rstrip()

dp_devil = [[0] * len(devil) for _ in range(len(ans))]
dp_angel = [[0] * len(angel) for _ in range(len(ans))]


for idx1, ch in enumerate(ans):
    count = 0
    for idx2, dev in enumerate(devil):
        if idx1 == 0:
            if idx2 == 0:
                if dev == ch:
                    count += 1
                    dp_devil[idx1][idx2] = count
            else:
                if dev == ch:
                    count += 1
                    dp_devil[idx1][idx2] = dp_devil[idx1][idx2-1] + 1
                else:
                    dp_devil[idx1][idx2] = dp_devil[idx1][idx2-1]
        else:
            if idx2 == 0:
                continue
            else:
                if dp_angel[idx1-1][idx2 - 1] > 0:
                    if dev == ch:
                        count += 1
                        dp_devil[idx1][idx2] = dp_angel[idx1-1][idx2 - 1] * count
                    else:
                        dp_devil[idx1][idx2] = dp_devil[idx1][idx2 - 1]


    count1 = 0
    for idx2, ang in enumerate(angel):
        if idx1 == 0:
            if idx2 == 0:
                if ang == ch:
                    count1 += 1
                    dp_angel[idx1][idx2] = count1
            else:
                if ang == ch:
                    count1 += 1
                    dp_angel[idx1][idx2] = dp_angel[idx1][idx2-1] + 1
                else:
                    dp_angel[idx1][idx2] = dp_angel[idx1][idx2-1]
        else:
            if idx2 == 0:
                continue
            else:
                if dp_devil[idx1-1][idx2 - 1] > 0:
                    if ang == ch:
                        count1 += 1
                        dp_angel[idx1][idx2] = dp_devil[idx1-1][idx2 - 1] * count1
                    else:
                        dp_angel[idx1][idx2] = dp_angel[idx1][idx2 - 1]

print(dp_devil)
print(dp_angel)
print(dp_devil[-1][-1] + dp_angel[-1][-1])
