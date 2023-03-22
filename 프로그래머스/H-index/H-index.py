def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, c in enumerate(citations):
        if (idx + 1) > c:
            answer = idx
            break
        elif idx + 1 == c:
            answer = c

    if answer == 0:
        answer = len(citations)

    if citations[0] == 0:
        answer = 0

    return answer