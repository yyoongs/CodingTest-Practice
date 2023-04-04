import heapq


def solution(book_time):
    answer = 1
    times = []
    for s, e in book_time:
        li = []
        hh, mm = map(int, s.split(":"))
        li.append(hh * 60 + mm)
        hh, mm = map(int, e.split(":"))
        li.append(hh * 60 + mm)
        times.append(li)
    qe = []
    times.sort(key=lambda x: x[0])
    heapq.heappush(qe, times[0][1] + 10)
    for ts, te in times[1:]:
        if qe[0] <= ts:
            heapq.heappop(qe)
        else:
            answer += 1
        heapq.heappush(qe, te + 10)

    return answer