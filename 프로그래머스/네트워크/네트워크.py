#재귀를 이용한 dfs
def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(curr):
        if visited[curr] == True:
            return
        else:
            visited[curr] = True

            for i in range(n):
                if computers[curr][i] == 1 and curr != i:
                    dfs(i)

    for j in range(n):
        if visited[j] == False:
            dfs(j)
            answer += 1

    return answer


#stack을 이용한 dfs
def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            answer += 1
            q = []
            q.append(i)
            while q:
                curr = q.pop()
                if visited[curr] == False:
                    visited[curr] = True
                    for j in range(n):
                        if curr != j and computers[curr][j] == 1:
                            q.append(j)

    return answer


#queue를 이용한 bfs
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(curr):
        q = deque()
        q.append(curr)
        while q:
            idx = q.popleft()
            visited[idx] = True
            for i in range(n):
                if idx != i and computers[idx][i] == 1 and visited[i] == False:
                    q.append(i)

    for i in range(n):
        if visited[i] == False:
            bfs(i)
            answer += 1

    return answer