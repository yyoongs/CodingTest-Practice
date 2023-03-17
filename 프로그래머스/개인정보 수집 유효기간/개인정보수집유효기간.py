def check_date(today, dates):
    todays = list(map(int, today.split(".")))
    if dates[0] < todays[0]:
        return False

    if dates[0] > todays[0]:
        return True

    if dates[0] == todays[0]:
        if dates[1] < todays[1]:
            return False

        if dates[1] > todays[1]:
            return True

        if dates[1] == todays[1]:
            if dates[2] < todays[2]:
                return False

            if dates[2] >= todays[2]:
                return True


def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for t in terms:
        name, length = t.split()
        term_dict[name] = length

    for idx, p in enumerate(privacies):
        date, term = p.split()
        dates = list(map(int, date.split(".")))
        lens = term_dict[term]
        dates[2] = int(dates[2]) - 1
        if dates[2] == 0:
            dates[2] = 28
            dates[1] -= 1
            if dates[1] == 0:
                dates[1] = 12
                dates[0] -= 1
        dates[1] += int(lens)
        if dates[1] > 12:
            if dates[1] % 12 == 0:
                dates[0] += ((dates[1] // 12) - 1)
                dates[1] = 12
            else:
                dates[0] += (dates[1] // 12)
                dates[1] = (dates[1] % 12)
        if not check_date(today, dates):
            answer.append(idx + 1)

    return answer