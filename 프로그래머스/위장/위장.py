def solution(clothes):
    answer = 0
    hashs = {}
    for c, types in clothes:
        if hashs.get(types):
            hashs[types] += 1
        else:
            hashs[types] = 1

    temp = 1
    for key, values in hashs.items():
        temp *= (values + 1)

    return temp - 1