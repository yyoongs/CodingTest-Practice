# [BOJ] 2661
# LEVEL : G4

#7

import sys

n = int(sys.stdin.readline())
INF = sys.maxsize
answer = INF
def dfs(string):
    global n

    if len(string) == n:
        print(string)
        exit()
    else:
        for i in range(1,4):
            string += str(i)
            limit = len(string) // 2
            flag = True
            for j in range(1,limit+1):
                if string[-j:] == string[-j*2:-j]:
                    string = string[:-1]
                    flag = False
                    break

            if flag:
                dfs(string)

dfs("1")

print(answer)