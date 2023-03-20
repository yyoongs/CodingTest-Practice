def solution(number, k):
    answer = ''
    temp = []
    first = 0
    second = 1
    for n in number:
        temp.append(int(n))
    l = len(temp)
    i = 0
    while i < k:
        if second >= len(temp) or first > (l - k):
            break
        if temp[first] == 9:
            first += 1
            second += 1

        elif temp[first] < temp[second]:
            temp.pop(first)
            i += 1
            if first > 0:
                first -= 1
                second -= 1
        elif temp[first] >= temp[second]:
            first += 1
            second += 1

    for p in temp:
        answer += str(p)

    return answer[:l - k]