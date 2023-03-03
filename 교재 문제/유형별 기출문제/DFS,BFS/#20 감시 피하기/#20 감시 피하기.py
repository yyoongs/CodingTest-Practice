

n = int(input())

graph = []
result = False

for _ in range(n):
    graph.append(list(map(str,input().split())))

# n = 5
# graph = [['X', 'S', 'X', 'X', 'T'], ['T', 'X', 'S', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'T', 'X', 'X', 'X'], ['X', 'X', 'T', 'X', 'X']]

def check_xy(x,y):
    global n, result

    while x > 0:
        x -= 1
        if graph[x][y] == "S":
            result = False
            return False
        elif graph[x][y] == "O":
            break

    while x < (n-1):
        x += 1
        if graph[x][y] == "S":
            result = False
            return False
        elif graph[x][y] == "O":
            break

    while y > 0:
        y -= 1
        if graph[x][y] == "S":
            result = False
            return False
        elif graph[x][y] == "O":
            break

    while y < (n-1):
        y += 1
        if graph[x][y] == "S":
            result = False
            return False
        elif graph[x][y] == "O":
            break

    return True


def check_result():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "T":
                if check_xy(i,j):
                    continue
                else:
                    return False
    return True


def dfs(i):
    global result

    if i == 3:
        print(graph)
        if not check_result():
            return "No"
        else:
            result = True
            return "Yes"
    else:
        for a in range(len(graph)):
            for b in range(len(graph)):
                if graph[a][b] == "X":
                    graph[a][b] = "O"
                    i+=1
                    dfs(i)
                    graph[a][b] = "X"
                    i-=1



dfs(0)
print(result)