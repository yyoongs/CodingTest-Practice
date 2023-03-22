def solution(brown, yellow):
    if yellow == 2:
        return [4, 3]
    if yellow == 1:
        return [3, 3]

    for i in range(yellow // 2, 1, -1):
        if yellow % i == 0:
            if (i + 2) * ((yellow // i) + 2) - yellow == brown:
                big = max(i, yellow // i)
                return [big + 2, (yellow // big) + 2]
