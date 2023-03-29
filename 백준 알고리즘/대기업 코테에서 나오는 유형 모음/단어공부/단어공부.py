import sys
char = sys.stdin.readline().rstrip()

hashs = {}
for c in char:
    ascii = ord(c)
    if ascii >= 97:
        ascii -= 32
    c = chr(ascii)
    if hashs.get(c):
        hashs[c] += 1
    else:
        hashs[c] = 1


hashs = sorted(hashs.items(), key=lambda x:x[1], reverse=True)

if len(hashs) == 0:
    print("?")

elif len(hashs) >= 2:
    if hashs[0][1] == hashs[1][1]:
        print('?')
    else:
        print(hashs[0][0])
else:
    print(hashs[0][0])