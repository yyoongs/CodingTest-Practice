# [BOJ] 5582
# LEVEL : G5

#empl1
# ABRACADABRA
# ECADADABRBCRDARA

#empl2
# UPWJCIRUCAXIIRGL
# SBQNYBSBZDFNEV

import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()

dp = [[0] * (len(first)+1) for _ in range(len(second)+1)]
answer = 0
for i in range(1,len(second)):
    for j in range(1,len(first)):
        if second[i] == first[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        answer = max(answer,dp[i][j])


print(answer)



# short = 0
# if len(first) >= len(second):
#     short = 2
# else:
#     short = 1
#
# answer = 0
# flag = False
# if short == 2:
#     for i in range(len(second),0,-1):
#         hm = set()
#         for j in range(0,len(first)-i+1):
#             hm.add(first[j:j+i])
#
#         for k in range(0, len(second) - i + 1):
#             if second[k:k + i] in hm:
#                 flag = True
#                 answer = i
#                 break
#
#         if flag:
#             break
#
# else:
#     for i in range(len(first), 0, -1):
#         hm = set()
#         for j in range(0, len(second) - i + 1):
#             hm.add(second[j:j + i])
#
#         for k in range(0, len(first) - i + 1):
#             if first[k:k + i] in hm:
#                 flag = True
#                 answer = i
#                 break
#
#         if flag:
#             break
#
#
# print(answer)