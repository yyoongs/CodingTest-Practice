from collections import deque


def solution(begin, target, words):
    visited = [False] * len(words)

    def replace_word(curr):
        ans = []
        for idx, w in enumerate(words):

            count = 0
            for idxx, c in enumerate(curr):
                if w[idxx] == c:
                    continue
                else:
                    count += 1
            if count == 1:
                ans.append([idx, w])

        return ans if len(ans) >= 1 else -1

    def bfs():
        q = deque()
        q.append([begin, 0])

        while q:
            nex, count = q.popleft()
            if nex == target:
                return count
            li = replace_word(nex)
            if li != -1:
                for idx, w in li:
                    if not visited[idx]:
                        q.append([w, count + 1])
                        visited[idx] = True
        return 0

    return bfs()