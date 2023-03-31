import sys

n,d,k,c = map(int,sys.stdin.readline().rstrip().split())

dishs = []
for _ in range(n):
    dishs.append(int(sys.stdin.readline().rstrip()))

dishs += dishs[0:k]

hashs = {}
hashs[c] = 1
answer = len(hashs)

for i in range(k):
    if hashs.get(dishs[i]):
        hashs[dishs[i]] += 1
    else:
        hashs[dishs[i]] = 1

for i in range(k,len(dishs)-1):
    if hashs.get(dishs[i]):
        hashs[dishs[i]] += 1
    else:
        hashs[dishs[i]] = 1

    hashs[dishs[i-k]] -= 1
    if hashs[dishs[i-k]] == 0:
        hashs.pop(dishs[i-k])

    answer = max(answer,len(hashs))

print(answer)