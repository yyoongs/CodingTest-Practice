n,k = map(int,input().split())

# DP
dp = [int(1e9)] * 200002
dp[0] = n
for i in range(1,len(dp)-1):
    if i <= n:
        dp[i] = n-i
    else:
        if i % 2 ==0:
            dp[i] = min(min(dp[i-1],dp[i+1])+1,dp[i//2])
        else:
            dp[i] = min(dp[i-1],dp[i+1]) + 1
    j = i
    while True:
        j = j*2
        if j > 200001:
            break
        else:
            dp[j] = min(dp[i],dp[j])

print(dp[k])

#다익스트라
import heapq
distance = [int(1e9)] * 100001
q = []
heapq.heappush(q,(0,n))
distance[n] = 0

while q:
    cost, idx = heapq.heappop(q)
    if idx+1 <= 100000 and distance[idx+1] > (cost+1):
        distance[idx + 1] = cost + 1
        heapq.heappush(q, (cost + 1, idx + 1))
    if 0<= idx-1 <= 100000 and distance[idx - 1] > (cost+1):
        distance[idx - 1] = cost + 1
        heapq.heappush(q, (cost + 1, idx - 1))
    if idx*2 <= 100000 and distance[idx * 2] > cost:
        distance[idx*2] = cost
        heapq.heappush(q, (cost, idx * 2))

print(distance[k])