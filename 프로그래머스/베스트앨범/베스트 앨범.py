def solution(genres, plays):
    answer = []
    hashs = {}
    for idx in range(len(genres)):
        if hashs.get(genres[idx]):
            hashs[genres[idx]][0] += plays[idx]
            hashs[genres[idx]][1].append((idx, plays[idx]))
        else:
            hashs[genres[idx]] = [plays[idx], [(idx, plays[idx])]]

    hashs = sorted(hashs.items(), key=lambda x: x[1][0], reverse=True)

    for g, val in hashs:
        val[1].sort(key=lambda x: x[1], reverse=True)
        if len(val[1]) == 1:
            answer.append(val[1][0][0])
        else:
            answer.append(val[1][0][0])
            answer.append(val[1][1][0])

    return answer