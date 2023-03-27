def solution(survey, choices):
    answer = ''
    score = {'A': 0, 'N': 0, 'J': 0, 'M': 0, 'C': 0, 'F': 0, 'R': 0, 'T': 0}

    def update_score(s, choice):
        if choice == 1:
            score[s[0]] += 3
        if choice == 2:
            score[s[0]] += 2
        if choice == 3:
            score[s[0]] += 1
        if choice == 5:
            score[s[1]] += 1
        if choice == 6:
            score[s[1]] += 2
        if choice == 7:
            score[s[1]] += 3

    for i in range(len(survey)):
        update_score(survey[i], choices[i])

    if score['T'] > score['R']:
        answer += 'T'
    else:
        answer += 'R'

    if score['F'] > score['C']:
        answer += 'F'
    else:
        answer += 'C'

    if score['M'] > score['J']:
        answer += 'M'
    else:
        answer += 'J'

    if score['N'] > score['A']:
        answer += 'N'
    else:
        answer += 'A'

    return answer