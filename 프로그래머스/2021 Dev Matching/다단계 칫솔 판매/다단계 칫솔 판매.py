def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    hashs = {}

    def get_parent(name):
        if referral[hashs[name]] == "-":
            return False
        else:
            return referral[hashs[name]]

    for idx, e in enumerate(enroll):
        hashs[e] = idx

    for idx, s in enumerate(seller):
        money = amount[idx] * 100
        while True:
            if not get_parent(s):
                answer[hashs[s]] += (money - int(money * 0.1))
                break
            else:
                if money == 0:
                    break
                answer[hashs[s]] += (money - int(money * 0.1))
                money -= (money - int(money * 0.1))
                s = get_parent(s)

    return answer