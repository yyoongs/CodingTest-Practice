import sys
import copy

n, k = map(int,sys.stdin.readline().rstrip().split())

belt = list(map(int,sys.stdin.readline().rstrip().split()))

pos = [0] * len(belt)

turn = 1


def rotate(data):
    temp = copy.deepcopy(data[:-1])
    temp = [data[-1]] + temp
    data = copy.deepcopy(temp)
    return data


def pop_robot():
    if pos[n-1] == 1:
        pos[n-1] = 0
    return


def insert_robot():
    if pos[0] == 0 and belt[0] > 0:
        pos[0] = 1
        belt[0] -= 1
    return


while True:
    if belt.count(0) >= k:
        print(turn)
        break

    belt = rotate(belt)
    pos = rotate(pos)

    pop_robot()

    for i in range(n-1,-1,-1):
        if i == len(belt)-1:
            if pos[i] == 1 and pos[0] == 0 and belt[0] > 0:
                pos[i] = 0
                pos[0] = 1
                belt[0] -= 1
        else:
            if pos[i] == 1 and pos[i+1] == 0 and belt[i+1] > 0:
                pos[i] = 0
                pos[i+1] = 1
                belt[i+1] -= 1

    pop_robot()

    if belt.count(0) >= k:
        print(turn)
        break

    insert_robot()

    if belt.count(0) >= k:
        print(turn)
        break
    else:
        turn += 1