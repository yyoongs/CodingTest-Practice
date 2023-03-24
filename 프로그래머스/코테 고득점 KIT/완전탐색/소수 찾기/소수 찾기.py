from itertools import permutations


def solution(numbers):
    answer = []

    li = []
    for n in numbers:
        li.append(n)

    def is_prime_num(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    result = []
    for i in range(len(li)):
        result += list(permutations(li, i + 1))

    for res in result:
        temp = ''
        for c in res:
            temp += c
        if is_prime_num(int(temp)):
            if int(temp) == 1 or int(temp) == 0:
                continue
            elif int(temp) not in answer:
                answer.append(int(temp))

    return len(answer)