import heapq

n = int(input())

q = []

heapq.heappush(q,1)
count = 0
prev = 0
while count != n:
    curr = heapq.heappop(q)
    if prev < curr:
        count += 1
        prev = curr

        next2 = curr*2
        next3 = curr*3
        next5 = curr*5

        heapq.heappush(q, next2)
        heapq.heappush(q, next3)
        heapq.heappush(q, next5)


print(curr)

