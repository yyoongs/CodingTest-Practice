import sys
import copy
n = int(sys.stdin.readline().rstrip())

li = []
for i in range(n):
    li.append(sys.stdin.readline().rstrip())

first = li[0]
hashs = {}
for c in first:
    if hashs.get(c):
        hashs[c] += 1
    else:
        hashs[c] = 1

answer = 0

for l in li[1:]:
    temp = copy.deepcopy(hashs)
    for c in l:
        if temp.get(c):
            temp[c] -= 1
        else:
            temp[c] = -1
    flag = False
    hash_t = [0,0]
    for key,val in temp.items():
        if val not in [-1,0,1]:
            flag = True
            break
        else:
            if val == 1:
                hash_t[1] += 1
            if val == -1:
                hash_t[0] += 1

    if not flag and hash_t in [[0,0],[1,0],[0,1],[1,1]]:
        answer += 1

print(answer)