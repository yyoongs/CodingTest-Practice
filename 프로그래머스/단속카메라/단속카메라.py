def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x: x[1])
    pos = routes[0][1]
    for s, e in routes:
        if s <= pos:
            continue
        else:
            answer += 1
            pos = e

    return answer