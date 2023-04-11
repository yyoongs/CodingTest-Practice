import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))

q = []

for d in data:
    if len(q) < n:
        flag = False
        for idx,[x,y] in enumerate(q):
            if x == d:
                q[idx][1] += 1
                flag = True
                break
        if not flag:
            q.append([d,1])
    else:
        flag = False
        for idx, [x,y] in enumerate(q):
            if x == d:
                q[idx][1] += 1
                flag = True
                break

        if not flag:
            mins = int(1e9)
            temp = -1
            for idx, [x,y] in enumerate(q):
                if y < mins:
                    temp = idx
                    mins = y
            q.pop(temp)
            q.append([d,1])

q.sort(key=lambda x:x[0])

for x in q:
    print(x[0],end=' ')
