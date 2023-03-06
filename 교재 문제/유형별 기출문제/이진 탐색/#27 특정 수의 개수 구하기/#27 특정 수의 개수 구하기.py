n,x = map(int,input().split())

data = list(map(int,input().split()))

start_idx = 0
start = 0
end = (n-1)
while start <= end:
    mid = (start + end) // 2
    if (data[mid] == x) and (mid == 0 or x > data[mid-1]):
        start_idx = mid
        break
    elif data[mid] >= x:
        end = mid -1
    elif data[mid] < x:
        start = mid + 1

print(start_idx)

end_idx = 0
start = 0
end = (n-1)
while start <= end:
    mid = (start + end) // 2
    if (data[mid] == x) and (mid == (n-1) or x < data[mid+1]):
        end_idx = mid
        break
    elif data[mid] > x:
        end = mid -1
    elif data[mid] <= x:
        start = mid + 1

print(end_idx)

print(end_idx-start_idx +1)

#2

from bisect import bisect_left, bisect_right

left_idx = bisect_left(data,x)
right_idx = bisect_right(data,x)

print(left_idx,right_idx)