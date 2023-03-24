def solution(phone_book):
    answer = True
    lengths = {}
    for p in phone_book:
        l = len(p)
        if lengths.get(l):
            lengths[l].append(p)
        else:
            lengths[l] = [p]

    for ph in phone_book:
        l = len(ph)
        for key, value in lengths.items():
            if key < l and ph[:key] in value:
                return False
    return True