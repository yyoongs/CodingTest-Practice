import sys

n = int(sys.stdin.readline().rstrip())

data = [0] + list(map(int,sys.stdin.readline().rstrip().split()))

answer = []
for i in range(n,0,-1):
    # print(data[i])
    temp = data[i]
    flag = False
    for j in range(i,0,-1):
        if temp < data[j]:
            answer.append(j)
            flag = True
            break
    if not flag:
        answer.append(0)

for k in range(len(answer)-1,-1,-1):
    print(answer[k],end=" ")
