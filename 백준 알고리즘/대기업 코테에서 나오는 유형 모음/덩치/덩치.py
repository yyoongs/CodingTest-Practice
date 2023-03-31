import sys

n = int(sys.stdin.readline().rstrip())

data = []
for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    data.append(temp)
#
# n = 5
# data= [[55,185],[58,183],[88,186],[60,175],[46,155]]

hashs = {}
for idx,val in enumerate(data):
    weight = val[0]
    height = val[1]
    count = 0

    for n_idx in range(len(data)):
        if n_idx != idx and weight < data[n_idx][0] and height < data[n_idx][1]:
            count += 1

    if hashs.get(count):
        hashs[count].append(idx)
    else:
        hashs[count] = [idx]


hashs = sorted(hashs.items(), key=lambda x:x[0])

rank = [0]* n
ans = 1
for h in hashs:
    val = h[0]
    for idx in h[1]:
        rank[idx] = h[0]+1

for r in rank:
    print(r,end=" ")
