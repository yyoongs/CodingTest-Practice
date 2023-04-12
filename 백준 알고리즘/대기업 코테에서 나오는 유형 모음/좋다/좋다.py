import sys

n = int(sys.stdin.readline().rstrip())

data = list(map(int,sys.stdin.readline().rstrip().split()))

hashs = {}

for i in range(len(data)):
    for j in range(i+1,len(data)):
        temp = data[i] + data[j]
        if hashs.get(temp):
            hashs[temp].append([i,j])
        else:
            hashs[temp] = [[i,j]]

count = 0
for idx,d in enumerate(data):
    if hashs.get(d):

        for x,y in hashs[d]:
            if idx != x and idx != y:
                count += 1
                break

print(count)