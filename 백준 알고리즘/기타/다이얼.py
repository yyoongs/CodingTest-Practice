# [BOJ] 5622
# LEVEL : B2

#empl1
# WA

#empl2
# UNUCIC


import sys

number = sys.stdin.readline().rstrip()

hm = {"A" : 4, "B" : 4, "C" : 4, "D" : 5, "E" : 5, "F" : 5,"G" : 6, "H" : 6, "I" : 6,"J" : 7, "K" : 7, "L" : 7,"M" : 8, "N" : 8, "O" : 8,"P" : 9, "Q" : 9, "R" : 9,"S" : 9, "T" : 10, "U" : 10,"V" : 10, "W" : 11, "X" : 11,"Y" : 11, "Z" : 11}

answer = 0
for ch in number:
    answer += hm[ch] - 1

print(answer)