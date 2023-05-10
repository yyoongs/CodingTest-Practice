# [BOJ] 1043
# LEVEL : G4

# 4 3
# 0
# 2 1 2
# 1 3
# 3 2 3 4

# 4 5
# 1 1
# 1 1
# 1 2
# 1 3
# 1 4
# 2 4 1


# 10 9
# 4 1 2 3 4
# 2 1 5
# 2 2 6
# 1 7
# 1 8
# 2 7 8
# 1 9
# 1 10
# 2 3 10
# 1 4

import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

truths = list(map(int,sys.stdin.readline().rstrip().split()))


hm = {}

if len(truths) != 1:
    for t in truths[1:]:
        hm[t] = True

parties = []
for i in range(m):
    member = list(map(int, sys.stdin.readline().rstrip().split()))
    parties.append(member[1:])

answer = []
def recursion(parties):
    global answer
    nexts = []
    people = []
    for party in parties:
        story = False
        for mem in party:
            if hm.get(mem):
                story = True

        if story:
            for mem2 in party:
                if hm.get(mem2):
                    continue
                else:
                    people.append(mem2)
        else:
            nexts.append(party)

    if nexts == parties:
        answer = nexts
        return
    else:
        for person in people:
            hm[person] = True
        recursion(nexts)

recursion(parties)

print(len(answer))


# union find
#
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 1 2 7 8 9 3

import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

truths = list(map(int,sys.stdin.readline().rstrip().split()))

parties = []
for i in range(m):
    member = list(map(int, sys.stdin.readline().rstrip().split()))
    parties.append(member[1:])

parent = [0] + [i for i in range(1,n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(x,y):
    nx = find(x)
    parent[y] = nx

if len(truths) != 1:
    truths = truths[1:]
else:
    truths = []

answer = []
checked = [False] * m


def unionfind(parties):
    first_num_false = m - sum(checked)
    for idx,party in enumerate(parties):
        story = False
        number = 0
        for mem in party:
            if find(mem) in truths:
                story = True
                number = find(mem)
                break

        if story:
            checked[idx] = True
            for mem2 in party:
                if find(mem2) not in truths:
                    union(number,mem2)
    second_num_false = m - sum(checked)
    if first_num_false == second_num_false:
        return
    else:
        unionfind(parties)

unionfind(parties)

print(m - sum(checked))