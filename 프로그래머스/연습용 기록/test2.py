kor = ["CCC", "BCDF"]
usa = ["XXXX"]
incs = ["BCDF CCC", "XXXX"]
hashs = {}
temp1 = []
temp2 = []
for inc in incs:
    stocks = inc.split()
    li1 = []
    li2 = []
    for stock in stocks:
        if stock in kor:
            li1.append(stock)
        else:
            li2.append(stock)

    temp1.append(li1)
    temp2.append(li2)

for day in range(len(incs)):

    for k in temp1[day]:
        for u in temp2[day]:
            keys = (k,u)
            if hashs.get(keys):
                hashs[keys] += 1
            else:
                hashs[keys] = 1

hashs = sorted(hashs.values())

if len(hashs) == 0:
    print(0)
else:
    print(hashs[-1])