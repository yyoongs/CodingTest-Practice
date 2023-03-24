def solution(triangle):
    height = len(triangle)
    sums = []
    for i in range(height):
        sums.append([0] * (i + 1))
    sums[0][0] = triangle[0][0]

    for level in range(1, len(triangle)):
        for i in range(len(sums[level])):
            if i == 0:
                sums[level][i] = sums[level - 1][i] + triangle[level][i]
            elif i == len(sums[level]) - 1:
                sums[level][i] = sums[level - 1][i - 1] + triangle[level][i]
            else:
                sums[level][i] = max(sums[level - 1][i - 1], sums[level - 1][i]) + triangle[level][i]

    return max(sums[-1])