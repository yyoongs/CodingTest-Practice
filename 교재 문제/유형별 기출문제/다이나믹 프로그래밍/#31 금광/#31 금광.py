t = int(input())

for _ in range(t):
    n,m = map(int,input().split())

    data = list(map(int,input().split()))
    maps = []
    for i in range(n):
        maps.append(data[(i*4):((i+1)*4)])


    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = maps[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = maps[i+1][j-1]
            left = maps[i][j-1]
            maps[i][j] = maps[i][j] + max(left_down,left,left_up)

    result = 0
    for i in range(n):
        result = max(result,maps[i][m-1])

    print(result)