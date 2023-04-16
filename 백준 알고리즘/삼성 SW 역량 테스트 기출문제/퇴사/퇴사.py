import sys

n = int(sys.stdin.readline().rstrip())

t = [0] * (n)
p = [0] * (n)
for i in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    t[i] = a
    p[i] = b
result = [0] * (n+1)
for i in range(n-1,-1,-1):
    if i + t[i] > n:
        result[i] = result[i+1]
    else:
        result[i] = max(result[i+1], p[i] + result[i+t[i]])

print(result[0])