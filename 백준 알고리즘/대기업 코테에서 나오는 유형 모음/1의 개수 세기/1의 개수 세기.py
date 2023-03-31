import sys
a,b = map(int,sys.stdin.readline().rstrip().split())
count = 0

for i in range(a,b+1):
    temp = bin(i)
    for t in temp[2:]:
        if t == '1':
            count += 1

print(count)