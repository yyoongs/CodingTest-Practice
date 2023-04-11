import sys
import math

n,m = map(int,sys.stdin.readline().rstrip().split())

data = list(map(int,sys.stdin.readline().rstrip().split()))
data.sort(reverse=True)
data += [0]
temp = 0
prev = data[0]
idx = 1
for d in data[1:]:

    curr = (prev - d) * idx

    if temp + curr >= m:
        k = math.ceil((m -temp) / idx)
        print(prev-k)
        break
        # 높이기
    else:
        temp += curr
        prev = d
        idx += 1
