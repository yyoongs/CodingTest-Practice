n = int(input())

data = list(map(int,input().split()))

start = 0
end = len(data)-1
check = False
result= 0
while start <= end:
    mid = (start + end) // 2

    if data[mid] == mid:
        result = mid
        check = True
        break
    elif data[mid] > mid:
        end = mid -1
    else:
        start = mid +1


if check:
    print(result)
else:
    print(-1)