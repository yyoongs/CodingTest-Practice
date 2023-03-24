def solution(array, commands):
    answer = []
    for s,e,k in commands:
        temp = array[(s-1):e]
        temp.sort()
        answer.append(temp[k-1])
    return answer