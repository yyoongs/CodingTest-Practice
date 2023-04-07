import sys

n = int(sys.stdin.readline().strip())

data = [0]
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

answer = [0] * (n+1)


def calculate(n):
    if n == 1:
        return data[1]
    if n == 2:
        return data[1] + data[2]
    if n == 3:
        return max(data[n-2] + data[n], data[n-1] + data[n])
    if n == 4:
        return max(data[n-3] + data[n-2] + data[n], data[n-3] + data[n-1] + data[n], data[n-2] + data[n])
    else:
        return max(answer[n-3]  + data[n-1] + data[n], answer[n-4] + data[n-2] + data[n], answer[n-2] + data[n])

for i in range(1,n+1):
    answer[i] = calculate(i)

print(answer[-1])
