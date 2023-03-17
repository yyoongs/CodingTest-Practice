n = str(input())

li = []
for i in n:
    li.append(int(i))

li.sort(reverse=True)

result = ""

if li[-1] == 0 and sum(li) % 3 == 0:
    for i in li:
        result += str(i)
    print(result)
else:
    print(-1)

