import sys

n = int(sys.stdin.readline().rstrip())

data = list(map(int,sys.stdin.readline().rstrip().split()))

start = 0
end = n-1

result = int(1e10)
answer = []
while start < end:
    temp = abs(data[start] + data[end])
    if temp < result:
        answer = [data[start],data[end]]
        result = temp
        if result == 0:
            break
    if data[start] + data[end] < 0:
        start += 1
    else:
        end -= 1

print(answer[0],answer[1])
