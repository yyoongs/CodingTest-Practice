import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    command = input().rstrip().split()

    if command[0] == 'push':
        stack.append(command[1])

    if command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            nums = stack.pop()
            print(nums)
            stack.append(nums)

    if command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            nums = stack.pop()
            print(nums)

    if command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if command[0] == "size":
        print(len(stack))



