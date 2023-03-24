def solution(sizes):
    sizes.sort(key=lambda x: x[0])

    max_w = 0
    max_h = 0

    for w, h in sizes:
        temp_w = max(max_w, w)
        temp_h = max(max_h, h)
        temp_ans = temp_w * temp_h

        temp_w2 = max(max_w, h)
        temp_h2 = max(max_h, w)
        temp_ans2 = temp_w2 * temp_h2

        if temp_ans >= temp_ans2:
            max_w = temp_w2
            max_h = temp_h2
        else:
            max_w = temp_w
            max_h = temp_h

    return max_w * max_h