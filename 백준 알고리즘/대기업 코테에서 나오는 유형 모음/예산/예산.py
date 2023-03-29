import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
budget = int(sys.stdin.readline().rstrip())

data.sort()
temp = budget
answer = 0
for idx,b in enumerate(data):
    if (n-idx)*b <= temp:
        temp -= b
    else:
        answer = temp // (n-idx)
        break

if answer == 0:
    print(data[-1])
else:
    print(answer)