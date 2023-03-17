def solution(s, skip, index):
    li = []
    for i in range(26):
        temp = chr(i+97)
        if temp not in skip:
            li.append(temp)
    ans = ""
    for ch in s:
        curr = li.index(ch)
        ans += li[curr+int(index)] if curr+int(index) < len(li) else li[(curr+int(index))%len(li)]
    return ans