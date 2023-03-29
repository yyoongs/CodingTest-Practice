import sys

n,k = sys.stdin.readline().rstrip().split()

li = []

for i in range(int(n)):
    data = sys.stdin.readline().rstrip().split()
    li.append((int(data[1]),int(data[2]),int(data[3]),int(data[0])))

li.sort(key=lambda x:(-x[0],-x[1],-x[2]))

rank = [0] * (int(n)+1)
temp = (li[0][0], li[0][1], li[0][2])
rank[li[0][3]] = 1
temp_r = 1
for idx,val in enumerate(li[1:]):
    if (val[0],val[1],val[2]) == temp:
        rank[val[3]] = temp_r
    else:
        temp = (val[0],val[1],val[2])
        temp_r = idx + 2
        rank[val[3]] = temp_r

print(rank[int(k)])