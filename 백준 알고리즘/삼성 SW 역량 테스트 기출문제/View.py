T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print("#", end="")
    print(test_case, end=" ")

    n = int(input())
    data = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(data) - 2):
        height = data[i]
        side_height = max(data[i - 2], data[i - 1], data[i + 1], data[i + 2])
        if (height - side_height) > 0:
            answer += height - side_height
    print(answer)