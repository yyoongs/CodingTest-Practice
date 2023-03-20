def solution(n, lost, reserve):
    count = 0
    lost.sort()
    reserve.sort()
    for l in lost:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)

    for curr in range(1, n + 1):
        if curr in lost:
            if curr in reserve:
                reserve.remove(curr)
                count += 1
                continue
            elif curr - 1 in reserve:
                reserve.remove(curr - 1)
                count += 1
            elif curr + 1 in reserve:
                reserve.remove(curr + 1)
                count += 1
        else:
            count += 1

    return count