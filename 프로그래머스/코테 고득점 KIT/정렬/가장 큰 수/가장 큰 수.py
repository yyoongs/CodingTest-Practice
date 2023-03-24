def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    number = list(map(lambda x: (x * 4)[:4], numbers))
    temp = []
    for idx, n in enumerate(number):
        temp.append((n, len(numbers[idx])))
    temp.sort(key=lambda x: x[0], reverse=True)

    for n, length in temp:
        answer += n[:length]

    if answer[0] == '0':
        answer = '0'

    return answer