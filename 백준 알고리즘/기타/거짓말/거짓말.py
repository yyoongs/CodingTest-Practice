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



