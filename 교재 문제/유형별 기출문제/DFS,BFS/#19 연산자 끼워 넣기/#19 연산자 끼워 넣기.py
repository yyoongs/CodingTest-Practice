# product를 사용한 방법 1

from itertools import product

n = int(input())

nums = list(map(int,input().split()))

a,b,c,d = map(int,input().split())


opers = {"+": a, "-":b,"x":c,"%":d}

oper = ["+","-","x","%"]

prods = list(product(oper,repeat=n-1))

available = []

for pr in prods:
    temp = {"+": 0, "-":0,"x":0,"%":0}
    for p in pr:
        temp[p] += 1

    if temp == opers:
        available.append(pr)

max_value = -1e9
min_value = 1e9

for ava in available:
    result = nums[0]

    for i in range(n-1):
        if ava[i] == "+":
            result += nums[i+1]
        if ava[i] == "-":
            result -= nums[i + 1]
        if ava[i] == "%":
            if result <0:
                result = -result
                result //= nums[i + 1]
                result = -result
            else:
                result //= nums[i + 1]
        if ava[i] == "x":
            result *= nums[i + 1]

    max_value = max(max_value,result)
    min_value = min(min_value,result)

print(max_value,min_value)


#DFS를 사용한 방법

n = int(input())

nums = list(map(int,input().split()))

a,b,c,d = map(int,input().split())

max_value = -1e9
min_value = 1e9

def dfs(i,now):
    global min_value,max_value,a,b,c,d

    if i==n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)

    else:
        if a > 0:
            a -= 1
            dfs(i+1,now+nums[i])
            a += 1
        if b > 0:
            b -= 1
            dfs(i+1,now -nums[i])
            b += 1
        if c > 0:
            c -= 1
            dfs(i+1,now * nums[i])
            c += 1
        if d >0:
            d -= 1
            dfs(i+1,int(now / nums[i]))
            d += 1

dfs(1,nums[0])

print(max_value,min_value)

