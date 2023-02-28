count = 0
temp = ""
result = ""


def check_correct(line):
    if len(line) == 0:
        return True
    if line[0] == ')':
        return False
    else:
        check = []
        check.append(line[0])
        for i in range(1, len(line)):
            if line[i] == "(":
                check.append(line[i])
            else:
                if len(check) == 0:
                    return False
                elif check[-1] == "(":
                    check.pop()
                else:
                    return False

        if len(check) == 0:
            return True


def bfs(line):
    global temp
    global count
    global result
    if line == "":
        return
    for i in range(len(line)):
        if line[i] == '(':
            count += 1
        else:
            count -= 1

        temp += line[i]

        if count == 0:
            if check_correct(temp):  # 올바를때
                result += temp
                temp = ""
                bfs(line[i + 1:])
                return
            else:  # 올바른게 아니라면 4-1
                temp2 = temp
                result += "("
                temp = ""
                bfs(line[i + 1:])
                result += ")"
                for i in range(1, len(temp2) - 1):
                    if temp2[i] == "(":
                        result += ")"
                    else:
                        result += "("
                return


def solution(p):
    bfs(p)
    return result

print(solution("(()())()"))