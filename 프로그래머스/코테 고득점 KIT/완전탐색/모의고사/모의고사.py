def solution(answers):
    answer = [[0, 1], [0, 2], [0, 3]]
    p1 = [1, 2, 3, 4, 5] * ((10000 // 5) + 1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * ((10000 // 7) + 1)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((10000 // 10) + 1)

    for idx, a in enumerate(answers):
        if p1[idx] == a:
            answer[0][0] += 1
        if p2[idx] == a:
            answer[1][0] += 1
        if p3[idx] == a:
            answer[2][0] += 1

    answer.sort(key=lambda x: x[0], reverse=True)

    result = [answer[0][1]]

    for ans, idx in answer[1:]:
        if ans == answer[0][0]:
            result.append(idx)
    return result