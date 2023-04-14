# [BOJ] 2018
# LEVEL : 실버5

n = int(input())
start = 1
end = 1
count = 1
sums = 1

while end < n:
    print(start,end)
    if sums == n:
        print("ff")
        end += 1
        count += 1
        sums += end
    elif sums < n:
        end += 1
        sums += end
    else:
        sums -= start
        start += 1



print(count)