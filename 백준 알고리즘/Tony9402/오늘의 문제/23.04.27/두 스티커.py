# [BOJ] 16937
# LEVEL : S3


# 10 9
# 4
# 2 3
# 1 1
# 5 10
# 9 11

import sys

h,w= map(int,sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
stickers = []
for i in range(n):
    h1, w2 = map(int, sys.stdin.readline().rstrip().split())
    stickers.append([h1*w2,h1,w2])

stickers.sort(reverse=True)
answer = 0

for j in range(len(stickers)):
    temp_h = h
    temp_w = w
    temp_ans = 0
    sticker = stickers[j]
    if temp_h >= sticker[1] and temp_w >= sticker[2]:
        temp_h -= sticker[1]
        temp_w -= sticker[2]
        if temp_h*w >= temp_w*h:
            temp_w = w
        else:
            temp_h = h
        temp_ans = sticker[0]
        for k in range(j + 1, len(stickers)):
            sticker2 = stickers[k]
            if (temp_h >= sticker2[1] and temp_w >= sticker2[2]) or (temp_h >= sticker2[2] and temp_w >= sticker2[1]):
                temp_ans += sticker2[0]
                answer = max(answer,temp_ans)
                break
    elif temp_h >= sticker[2] and temp_w >= sticker[1]:
        temp_h -= sticker[2]
        temp_w -= sticker[1]
        if temp_h*w >= temp_w*h:
            temp_w = w
        else:
            temp_h = h
        temp_ans = sticker[0]
        for k in range(j + 1, len(stickers)):
            sticker2 = stickers[k]
            if (temp_h >= sticker2[1] and temp_w >= sticker2[2]) or (temp_h >= sticker2[2] and temp_w >= sticker2[1]):
                temp_ans += sticker2[0]
                answer = max(answer,temp_ans)
                break
    else:
        continue

print(answer)

