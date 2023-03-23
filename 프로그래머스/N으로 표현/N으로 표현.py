def solution(N, number):
    if N == number:
        return 1

    avail_set = {}

    for i in range(1, 9):
        avail_set[i] = set()
    avail_set[1].add(N)

    for i in range(2, 9):
        temp_set = set()
        if int(str(N) * i) == number:
            return i
        temp_set.add(int(str(N) * i))
        for n in range(1, i):
            temp1 = avail_set[n]
            temp2 = avail_set[i - n]

            for t1 in temp1:
                for t2 in temp2:
                    if t2 == 0:
                        if t1 * t2 == number or t1 + t2 == number or t1 - t2 == number:
                            return i
                        temp_set.add(t1 * t2)
                        temp_set.add(t1 + t2)
                        temp_set.add(t1 - t2)
                    else:
                        if t1 * t2 == number or t1 + t2 == number or t1 // t2 == number or t1 - t2 == number:
                            return i
                        temp_set.add(t1 * t2)
                        temp_set.add(t1 // t2)
                        temp_set.add(t1 + t2)
                        temp_set.add(t1 - t2)

        avail_set[i] = temp_set

    return -1
