from collections import deque

# 큐를 이용한 bfs
def solution(numbers, target):
    answer = 0

    q = deque()

    q.append([numbers[0], 0])
    q.append([(-1) * numbers[0], 0])

    while q:
        temp, idx = q.popleft()
        if idx == len(numbers) - 1:
            if temp == target:
                answer += 1
        else:
            q.append([temp + numbers[idx + 1], idx + 1])
            q.append([temp - numbers[idx + 1], idx + 1])

    return answer


# 재귀를 이용한 bfs
def solution(numbers, target):
    answer = 0

    def dfs(temp, idx):
        nonlocal answer
        if idx == len(numbers) - 1:
            if temp == target:
                answer += 1
        else:
            dfs(temp + numbers[idx + 1], idx + 1)
            dfs(temp - numbers[idx + 1], idx + 1)

    dfs(numbers[0], 0)
    dfs((-1) * numbers[0], 0)

    return answer


# stack을 이용한 dfs
def solution(numbers, target):
    answer = 0
    q = [[numbers[0], 0], [(-1) * numbers[0], 0]]

    while q:
        temp, idx = q.pop()
        if idx == len(numbers) - 1:
            if temp == target:
                answer += 1
        else:
            q.append([temp + numbers[idx + 1], idx + 1])
            q.append([temp - numbers[idx + 1], idx + 1])

    return answer

