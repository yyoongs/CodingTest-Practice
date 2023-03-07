import sys

# 입력 받기
n = int(input())

times = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    times.append((start,end))

# 끝나는시간 오름차순 / 시작시간 오름차순 정렬 ( 시간복잡도 O(nlogn) )
times = sorted(times, key=lambda x: (x[1], x[0]))

count = 1
end_time = times[0][1]
for i in range(1,len(times)): # times list를 돌면서 시작 시간이 이전 끝나는 시간보다 크면 count +1 & end_time 재설정 (시간복잡도 O(n))
    if times[i][0] >= end_time:
        count +=1
        end_time = times[i][1]

print(count)

# 총 시간복잡도 = O(nlogn) => 정렬하는데 가장 오래걸림