# bfs 사용
# 연합 저장
# 연합 인구수 계산
# 만약 연합에 들어있지 않다면
from collections import deque
import copy
n,l,r = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
# n,l,r = 4,10,50
# graph = [[10, 100, 20, 90], [80, 100, 60, 70], [70, 20, 30, 40], [50, 20, 100, 10]]
temp = []
count = 0
dx = [0,-1,0,1]
dy = [1,0,-1,0]


# 방문한 노드인지 확인
def check_visited(x,y):
    for c, (tx,ty) in temp:
        if (tx,ty) == (x,y):
            return False

    return True

#DFS 활용
def dfs(x,y):
    global n, l ,r, count
    if check_visited(x,y):

        q = deque([[x,y]])
        temp.append((count, (x,y)))
        while q:
            cx,cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if nx >=0 and nx < len(graph) and ny>=0 and ny < len(graph):
                    if l <= abs(graph[cx][cy] - graph[nx][ny]) <= r and check_visited(nx,ny):
                        temp.append((count,(nx,ny)))
                        q.append([nx,ny])
                else:
                    continue

        count += 1

t = 0
while True: # 인구이동 횟수 확인
    graph_t = copy.deepcopy(graph) # 배열 딥카피
    print(graph_t)
    for i in range(n):
        for j in range(n):
            dfs(i,j) # 각턴마다 모든 위치에서 dfs 실행

    temp_l = []
    temp_i = 0
    for a,(b,c) in temp: # 저장된 temp 리스트를 통해 인구 업데이트
        if temp_i == a:

            temp_l.append((b,c))
        else:
            sums = 0
            for c,d in temp_l:
                sums += graph[c][d]
            sums = int(sums/len(temp_l))

            for c,d in temp_l:
                graph[c][d] = sums

            temp_i = a
            temp_l = [(b,c)]

    # 마지막 남은 그룹 업데이트
    sums = 0
    for c, d in temp_l:
        sums += graph[c][d]
    sums = int(sums / len(temp_l))

    for c, d in temp_l:
        graph[c][d] = sums
    print(graph)
    print(graph_t)

    # 만약 변한게 없다면 인구이동이 없는 것이므로 시간 print후 리턴
    if graph_t == graph:
            print(t)
            break
    else:
        t += 1
        temp = []
        count = 0


print(graph)
print(temp)