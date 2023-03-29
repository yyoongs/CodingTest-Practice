n = int(input())

count = 0
i = 0
temp = 1
while True:
    temp = temp + 6 * i
    count += 1
    if temp >= n:
        break
    else:
        i += 1

print(count)