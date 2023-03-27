def solution(lottos, win_nums):
    answer = []
    correct = 0
    zeros = 0
    for n in lottos:
        if n == 0:
            zeros += 1
        elif n in win_nums:
            correct += 1
    if correct == 0 and zeros == 0:
        answer = [6,6]
    else:
        answer.append(7-(correct+zeros))
        if correct == 0:
            answer.append(6)
        else:
            answer.append(7-correct)

    return answer