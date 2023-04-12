import sys
import heapq

n = int(sys.stdin.readline().rstrip())

rightheap = []
leftheap = []
first = int(sys.stdin.readline().rstrip())
print(first)
heapq.heappush(leftheap,(-1)* first)
for i in range(n-1):
    mid = (-1) * leftheap[0]
    next = int(sys.stdin.readline().rstrip())
    if next >= mid:
        heapq.heappush(rightheap, next)
    else:
        heapq.heappush(leftheap, (-1)*next)

    if len(rightheap) - len(leftheap) == 1:
        temp = heapq.heappop(rightheap)
        heapq.heappush(leftheap, (-1) * temp)
    elif len(rightheap) - len(leftheap) == -2:
        temp = heapq.heappop(leftheap)
        heapq.heappush(rightheap, (-1) * temp)
    print((-1) * leftheap[0])
