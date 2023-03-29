import sys

li = [False] * 21

n=int(sys.stdin.readline().rstrip())

for _ in range(n):
    inputs = sys.stdin.readline().strip().split()
    if inputs[0] == 'add':
        li[int(inputs[1])] = True
    if inputs[0] == 'remove':
        li[int(inputs[1])] = False
    if inputs[0] == 'check':
        if li[int(inputs[1])]:
            print(1)
        else:
            print(0)
    if inputs[0] == 'toggle':
        li[int(inputs[1])] = not li[int(inputs[1])]
    if inputs[0] == 'all':
        for i in range(1,21):
            li[i] = True
    if inputs[0] == 'empty':
        for i in range(1, 21):
            li[i] = False

