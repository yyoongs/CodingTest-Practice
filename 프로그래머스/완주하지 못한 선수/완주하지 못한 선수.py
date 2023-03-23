def solution(participant, completion):
    answer = ''
    hash_set = {}
    for p in participant:
        if hash_set.get(p):
            hash_set[p] += 1
        else:
            hash_set[p] = 1

    for c in completion:
        if hash_set.get(c):
            hash_set[c] -= 1

    for key, value in hash_set.items():
        if value == 1:
            return key


# counter 활용

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
