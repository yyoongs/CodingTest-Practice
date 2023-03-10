n = int(input())

path = list(map(int,input().split()))
cost = list(map(int,input().split()))

result = 0
sum_road = 0
curr = 1
min_cost = cost[0]

while curr <= n-1:
    next_cost = cost[curr]

    if min_cost < next_cost:
        sum_road += path[curr-1]
        curr += 1
    else:
        result += (sum_road + path[curr - 1]) * min_cost
        min_cost = next_cost
        sum_road = 0
        curr += 1

if sum_road > 0:
    result += sum_road * min_cost

print(result)